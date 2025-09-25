from pydantic import BaseSettings

class Settings(BaseSettings):
    postgres_host: str = 'postgres'
    postgres_port: int = 5432
    postgres_user: str = 'transit'
    postgres_password: str = 'transit'
    postgres_db: str = 'transitdb'
    kafka_broker: str = 'kafka:9092'
    secret_key: str = 'supersecret'

settings = Settings()
