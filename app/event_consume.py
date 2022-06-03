from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from app.kafka.consumer import AIOConsumer
from app.kafka.models.event import EventMessage
from app.core.config import settings
from confluent_kafka.schema_registry import SchemaRegistryClient


def commit_completed(err, partitions):
    if err:
        print(err)
    else:
        print('Committed partition offsets: %s', str(partitions))


schema_client = SchemaRegistryClient({
        'url': settings.SCHEMA_REGISTRY_URL,
        'basic.auth.user.info': settings.SCHEMA_REGISTRY_BASIC_AUTH_USER_INFO
    })
market_schema = schema_client.get_schema(settings.CONFLUENT_SCHEMA_ID)
json_deserializer = JSONDeserializer(market_schema.schema_str, from_dict=EventMessage.from_dict)


def process_message(msg: EventMessage):
    # TODO implement logic
    print(msg.__dict__)


consumer = AIOConsumer({
    'bootstrap.servers': settings.BOOTSTRAP_SERVERS,
    'security.protocol': settings.CONFLUENT_SECURITY_PROTOCOL,
    'sasl.mechanisms': settings.SASL_MECHANISMS,
    'sasl.username': settings.CONFLUENT_API_KEY,
    'sasl.password': settings.CONFLUENT_API_SECRET,
    'key.deserializer': StringDeserializer('utf_8'),
    'value.deserializer': json_deserializer,
    'group.id': settings.CONFLUENT_GROUP_ID,
    'enable.auto.commit': False,
    'auto.offset.reset': 'latest',
    'on_commit': commit_completed
}, [settings.TOPIC_NAME], process_message)


consumer.consume()

