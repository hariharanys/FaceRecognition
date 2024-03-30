from minio import Minio
from minio.error import S3Error
from utils.generic import minio_base_url
from middleware.errorHandling import ErrorHandling
import os

minio_client = Minio(os.getenv('MINIO_HOST')+":"+os.getenv('MINIO_PORT_WEB'),
                     access_key=os.getenv('MINIO_ACCESS_KEY'),
                     secret_key=os.getenv('MINIO_SECRET_KEY'),
                     secure=False)

def find_similar_images(db_folder,bucket_name):
    try:
        objects = minio_client.list_objects(bucket_name=bucket_name,prefix=db_folder,recursive=True)
        return objects
    except S3Error as e:
       error_code = getattr(e,'code',500)
       error_message = str(e)
       return ErrorHandling.handle_error(error_code=error_code,error_message=error_message)
