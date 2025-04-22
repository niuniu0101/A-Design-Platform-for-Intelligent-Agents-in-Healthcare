# import os
# from dotenv import load_dotenv

# load_dotenv('.env')

class Config:
    # DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    VECTORSTORE1_PATH = "/vectordb/vector_db_1"
    VECTORSTORE2_PATH = "/vectordb/vector_db_2"
    DATA = {
        "csv": "/data/health_check_data.csv",
        "pdf": "/data/symptoms.pdf"
    }