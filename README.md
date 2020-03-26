# Lambda-Function-for-S3-Create-object-Trigger

The aim is to store s3 object(i.e .json or .csv files) data to DynamoDB table whenever we upload an object to s3 bucket.

Requrements:

1) We need to create a DaynamoDB table.
2) Create IAM policies for S3, cloudwatchlogs & daynamoDB.
3) Create a role for Lambda service with above polices.
4) Create an S3 Bucket.
5) Create a lambda fuction & add the src code to lambda function.
6) Upload .csv or .json file to the bucket.
