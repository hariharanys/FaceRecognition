from flask import (jsonify,Response,request)
import numpy as np
import os
from middleware.errorHandling import ErrorHandling
from PIL import Image
import cv2
import tempfile
from handlers.fileStorage import find_similar_images
from packages.deepface.deepface import DeepFace
from urllib.parse import urljoin

def imageDetection():
    models = [
    "VGG-Face", 
    "Facenet", 
    "Facenet512", 
    "OpenFace", 
    "DeepFace", 
    "DeepID", 
    "ArcFace", 
    "Dlib", 
    "SFace",
    "GhostFaceNet",
    ]
    try:
        similarity_images = []
        minio_url = 'http://localhost:9004/'
        os.makedirs(os.getenv('TEMP_DIR'),exist_ok=True)
        if 'image' not in request.files:
            return ErrorHandling.handle_error(error_code=404)
        image = request.files['image']
        image_path = os.path.join(os.getenv('TEMP_DIR'),'uploaded_image.JPG')
        image.save(image_path)
        reference_image_path = os.path.join(os.getenv('TEMP_DIR'),'IMG_8363.JPG')
        if not os.path.exists(reference_image_path):
            return ErrorHandling.handle_error(error_code=404,error_message='img2 path mismatch')
        #result = DeepFace.verify(img1_path=image_path,img2_path=reference_image_path,model_name=models[3])
        objects = find_similar_images(db_folder='Photos',bucket_name='facerecognization')
        for obj in objects:
            if obj.object_name.endswith('.jpg') or obj.object_name.endswith('.jpeg') or obj.object_name.endswith('.png'):
                image_url = urljoin(minio_url, obj.bucket_name + '/' + obj.object_name)
                print(image_url)
        return jsonify({"faces":'ver'})
    except Exception as e:
       error_code = getattr(e,'code',500)
       error_message = str(e)
       return ErrorHandling.handle_error(error_code=error_code,error_message=error_message)