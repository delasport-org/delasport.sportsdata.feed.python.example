from confluent_kafka import DeserializingConsumer, KafkaException, KafkaError
import sys


class AIOConsumer:
    def __init__(self, configs, topics, msg_process):
        self._consumer = DeserializingConsumer(configs)
        self._cancelled = False
        self._topics = topics
        self._msg_process = msg_process

    def _consume_loop(self):
        try:
            self._consumer.subscribe(self._topics)

            while not self._cancelled:
                msg = self._consumer.poll(timeout=1.0)
                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                         (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    self._msg_process(msg.value())
                    self._consumer.commit(asynchronous=True)
        finally:
            # Close down consumer to commit final offsets.
            self._consumer.close()

    def close(self):
        self._cancelled = True

    def consume(self):
        self._consume_loop()
