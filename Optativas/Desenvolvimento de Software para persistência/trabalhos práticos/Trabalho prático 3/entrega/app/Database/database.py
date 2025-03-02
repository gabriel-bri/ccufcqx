from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
DB_NAME = os.getenv("DB_NAME")

if not DATABASE_URL or not DB_NAME:
    raise ValueError("Variáveis de ambiente DATABASE_URL ou DB_NAME não configuradas corretamente.")


client = AsyncIOMotorClient(DATABASE_URL)

db = client[DB_NAME]