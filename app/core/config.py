from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):

    CONFLUENT_SECURITY_PROTOCOL = 'SASL_SSL'
    SASL_MECHANISMS = 'PLAIN'

    # Schema Registry
    SCHEMA_REGISTRY_URL: str
    SCHEMA_REGISTRY_BASIC_AUTH_USER_INFO: str
    CONFLUENT_SCHEMA_ID: int

    # Kafka
    BOOTSTRAP_SERVERS: str
    CONFLUENT_API_KEY: str
    CONFLUENT_API_SECRET: str
    CONFLUENT_GROUP_ID: str
    TOPIC_NAME: str

    class Config:
        case_sensitive = True


settings = Settings()
