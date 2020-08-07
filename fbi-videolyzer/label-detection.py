# coding: utf-8
import boto3
session = boto3.Session(profile_name='fbiPythonAutomation')
=======
session = boto3.Session(profile_name='fbiAgent')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='fbivideolyzervideos')
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/saanabar/Downloads/*.mp4')
pathname = '~/Downloads/fbiShortVideo.mp4'
path = Path(pathname).expanduser().resolve()
print (path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object':{'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result ['Labels']
len(result['Labels'])
