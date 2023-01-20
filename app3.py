#for extracting contents in key value pair format

# from flask import Flask, jsonify
# import boto3
# import time
# from trp import Document
# app = Flask(__name__)


# @app.route("/")
# def home():

#     # Document
#     s3BucketName = "naveen-chaurasia-bucket"
#     documentName = "1645ed46_cd9c_496e_a1c3_4e637fb0c541_w461c132_r1_3_inch_camlock_pipe.pdf"
#     # Amazon Textract client
#     textract = boto3.client('textract')
#     # Call Amazon Textract
#     response = textract.analyze_document(
#     Document={
#     'S3Object': {
#     'Bucket': s3BucketName,
#     'Name': documentName
#     }
#     },
#     FeatureTypes=["FORMS"])
#     #print(response)
#     doc = Document(response)
#     return doc
 
import boto3
from trp import Document
# Document
s3BucketName = "<Your bucket name>"
documentName = "<Image with text>"
# Amazon Textract client
textract = boto3.client('textract')
# Call Amazon Textract
response = textract.analyze_document(
 Document={
 'S3Object': {
 'Bucket': "naveen-chaurasia-bucket",
 'Name': "1645ed46_cd9c_496e_a1c3_4e637fb0c541_w461c132_r1_3_inch_camlock_pipe.pdf"
 }
 },
 FeatureTypes=["FORMS"])
#print(response)
doc = Document(response)
for page in doc.pages:
 # Print fields
 print("Fields:")
 for field in page.form.fields:
  print("Key: {}, Value: {}".format(field.key, field.value))
# # Get field by key
#  print("\nGet Field by Key:")
#  key = "Phone Number:"
#  field = page.form.getFieldByKey(key)
#  if(field):
#   print("Key: {}, Value: {}".format(field.key, field.value))
# # Search fields by key
#  print("\nSearch Fields:")
#  key = "address"
#  fields = page.form.searchFieldsByKey(key)
#  for field in fields:
#   print("Key: {}, Value: {}".format(field.key, field.value))

