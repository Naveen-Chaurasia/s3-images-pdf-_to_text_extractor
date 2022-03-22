from flask import Flask, jsonify
import boto3
import time
app = Flask(__name__)



@app.route("/")
def home():

    s3BucketName = "naveen-chaurasia-bucket"
    documentName = "1647404296550-A._P._J._Abdul_Kalam_-_Wikipedia.pdf"

    # Amazon Textract client
    textract = boto3.client('textract',region_name='us-east-1')

    # Call Amazon Textract
    response = textract.start_document_text_detection(
    DocumentLocation={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })

    # data=[]
    # # Print detected text
    # for item in response["Blocks"]:
    #     if item["BlockType"] == "LINE":
    #         #print ('\033[94m' +  item["Text"] + '\033[0m')
    #         data.append(item["Text"])
    #         print(item["Text"])
            
        
    # return jsonify({"data":data})
    jobId= response["JobId"]



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




    # for resultPage in pages:
    #    for item in resultPage["Blocks"]:
    #       if item["BlockType"] == "LINE":
    #         print ('\033[94m' +  item["Text"] + '\033[0m')


    return jsonify({"data":pages})


    