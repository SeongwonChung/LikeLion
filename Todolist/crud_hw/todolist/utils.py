from crud_hw.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME,AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime as dt
from .models import Todolist, Comment
from django.contrib.auth.models import User

def upload_img(request, file_to_upload):
    #make client
    session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
    )

    s3 = session.resource('s3')

    # s3에 object 업로드
    user_pk = str(request.user.pk)+'/'
    timekey = dt.now().strftime("%Y%H%M%S")+'/'
    img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key = user_pk + timekey + file_to_upload.name,
        Body = file_to_upload
    )

    s3_img_url = 'https://sw-todolist.s3.ap-northeast-2.amazonaws.com/' + user_pk + timekey +file_to_upload.name

    return s3_img_url
