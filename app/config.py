import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY=os.getenv()
    AWS_ACCESS_KEY=os.getenv()
    AWS_SECRET_KEY=os.getenv()
    AWS_BUCKET_NAME=os.getenv()
    VECTOR_DB_PATH="vector_db"