import boto3
import json
import re

s3Client=boto3.client('s3')
dynamodb=boto3.resource('dynamodb')
tableName= dynamodb.Table('CompanyDetails')

# Returns the file format
def objectFormat(FileName):
    fileFormat = re.search(r'(?<=\.)\w+', FileName)
    return fileFormat.group()

# Write the JSON file data into Dynamodb DB
def JsonFunction(bucket,FileName):
    jsonObject = s3Client.get_object(Bucket=bucket,Key=FileName)
    jsonFileData = jsonObject['Body'].read()
    jsonDict = json.loads(jsonFileData)
    tableName.put_item(Item=jsonDict)

# Write the CSV file data into Dynamodb DB
def CsvFunction(bucket,FileName):
    csvObject = s3Client.get_object(Bucket=bucket,Key=FileName)
    csvData=csvObject['Body'].read().decode("utf-8")
    companies=csvData.split("\n")
    for company in companies:
        companyData=company.split(",")
        tableName.put_item(
            Item= {
                "CompanyID" : companyData[0],
                "CompanyName" : companyData[1],
                "Founded" : companyData[2],
                "Type" : companyData[3],
                "Industry" : companyData[4]
            }
        )

def lambda_handler(event, context):
    bucket=event['Records'][0]['s3']['bucket']['name']
    FileName=event['Records'][0]['s3']['object']['key']
    fileFormat=objectFormat(FileName)
    if fileFormat=='json':
        JsonFunction(bucket,FileName)
    elif fileFormat=='csv':
        CsvFunction(bucket,FileName) 
    else:
        pass
    