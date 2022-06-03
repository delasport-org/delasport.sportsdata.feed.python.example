B2B Kafka feed
==============

## Base requirements
* python: ^3.8
* confluent-kafka
* jsonschema
* requests
* pydantic

### Set up project
* [install docker](https://docs.docker.com/engine/install/)
* [install docker-compose](https://docs.docker.com/compose/install/)

### Docker Compose
* Build all containers: `docker-compose build`
* Run one container: `docker-compose run --rm <service-name>`
* Run all php consumers `docker-compose up -d`

### Development
```bash
# Add environment variables
      SCHEMA_REGISTRY_URL: ''
      SCHEMA_REGISTRY_BASIC_AUTH_USER_INFO: ''
      CONFLUENT_SCHEMA_ID: ''
      BOOTSTRAP_SERVERS: ''
      CONFLUENT_API_KEY: ''
      CONFLUENT_API_SECRET: ''
      CONFLUENT_GROUP_ID: ''
  
# Launch container
docker-compose run --rm <service-name> bash

# Inside the container
cd /var/www/app && composer install
bin/console $BUILDER_TYPE --break
```
