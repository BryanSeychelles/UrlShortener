from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

def GetEnv(key: str) -> str:
    if key == "database":
        obj = {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DATABASE_OWNER_PASSWORD")
        }
        return obj
    else:
        raise Exception("Select an category for the environment variable.")
