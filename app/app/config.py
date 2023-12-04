from dataclasses import dataclass

from environs import Env


@dataclass
class Database:
    host: str
    user: str
    name: str
    port: str
    password: str


@dataclass
class Config:
    db: Database


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    return Config(
        db=Database(
            host=env.str("POSTGRES_HOST"),
            user=env.str("POSTGRES_USER"),
            name=env.str("POSTGRES_DB"),
            port=env.str("POSTGRES_PORT"),
            password=env.str("POSTGRES_PASSWORD"),
        ),

    )
