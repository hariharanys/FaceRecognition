import os

def minio_base_url():
    return "https://"+os.getenv('MINIO_HOST_URL')+':'+os.getenv('MINIO_PORT_WEB')