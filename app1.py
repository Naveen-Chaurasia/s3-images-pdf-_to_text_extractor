#For json as a response
from flask import Flask, jsonify
import boto3
import time
app = Flask(__name__)
def startJob(s3BucketName, objectName):
    response = None
    client = boto3.client('textract',region_name='us-east-1')
    response = client.start_document_text_detection(
    DocumentLocation={
        'S3Object': {
            'Bucket':  s3BucketName,
            'Name': objectName
        }
    })
    return response["JobId"]
def isJobComplete(jobId):
    time.sleep(5)
    client = boto3.client('textract',region_name='us-east-1')
    response = client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]
    print("Job status: {}".format(status))
    while(status == "IN_PROGRESS"):
        time.sleep(5)
        response = client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]
        print("Job status: {}".format(status))
    return status
def getJobResults(jobId):
    pages = []
    time.sleep(5)
    client = boto3.client('textract',region_name='us-east-1')
    response = client.get_document_text_detection(JobId=jobId)
    
    pages.append(response)
    print("Resultset page recieved: {}".format(len(pages)))
    nextToken = None
    if('NextToken' in response):
        nextToken = response['NextToken']
    while(nextToken):
        time.sleep(5)
        response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)
        pages.append(response)
        print("Resultset page recieved: {}".format(len(pages)))
        nextToken = None
        if('NextToken' in response):
            nextToken = response['NextToken']
    return pages
# Document
s3BucketName = "naveen-chaurasia-bucket"
documentName = "1645ed46_cd9c_496e_a1c3_4e637fb0c541_w461c132_r1_3_inch_camlock_pipe.pdf"
@app.route("/")
def home():
    jobId = startJob(s3BucketName, documentName)
    print("Started job with id: {}".format(jobId))
    if(isJobComplete(jobId)):
        response = getJobResults(jobId)
    #print(response)
    # return response
    return jsonify({"data":response})
    # # Print detected text
    # for resultPage in response:
    #     for item in resultPage["Blocks"]:
    #         if item["BlockType"] == "LINE":
    #             print ('\033[94m' +  item["Text"] + '\033[0m')