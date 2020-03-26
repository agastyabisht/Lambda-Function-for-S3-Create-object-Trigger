# Lambda-Function-for-S3-Create-object-Trigger

The aim is to store s3 object(i.e .json or .csv files) data to DynamoDB table whenever we upload an object to s3 bucket.

Requrements

We need to create a DaynamoDB table.
Create IAM policies for S3, cloudwatchlogs & daynamoDB.
Create a role for Lambda service with above polices.
Create an S3 Bucket.
Create a lambda fuction & add the src code to lambda function.
Upload .csv or .json file to the bucket.
