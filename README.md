# Comprehend serverless Example
This is an Image detection app that uses Rekognition APIs to detect text in S3 Objects, stores labels in DynamoDB and sends SNS topic.
Person need to create the SNS topic manually and add the ARN to src/app.py file

## Requirements
This code need minimum Python 3.9 version

## Design Diagram
![design](https://user-images.githubusercontent.com/108154106/183280020-1897cdad-62a5-430e-8948-15f42a5e05e2.png)



## Project structure
Here is a code overview:
```bash
.
├── src                         <-- Source code for the Lambda function
│   ├── __init__.py
│   └── app.py                  <-- Lambda function code
├── template.yaml               <-- SAM template
└── SampleEvent.json            <-- Sample S3 event
```



First, we need an `S3 bucket` where we can upload our Lambda functions packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Next, run the following command to package your Lambda function. The `sam package` command creates a deployment package (ZIP file) containing your code and dependencies, and uploads them to the S3 bucket you specify. 

```bash
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```
![sam package](https://user-images.githubusercontent.com/108154106/183280054-57ee1403-8983-4fe1-b4d3-3b9bb7f4af32.png)

The `sam deploy` command will create a Cloudformation Stack and deploy your SAM resources.
```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name aws_sam_ocr \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides MyParameterSample=MySampleValue
```
![sam deploy1](https://user-images.githubusercontent.com/108154106/183280072-4aacc325-e578-4c4f-898b-07387c538df5.png)
![sam deploy2](https://user-images.githubusercontent.com/108154106/183280074-1ff006e5-cca7-40ec-8d92-d0f0c8b24776.png)

## S3 Bucket created by SAM deployment
![s3](https://user-images.githubusercontent.com/108154106/183280089-558f0b52-6ebc-48f4-b43c-f6f7444cea30.png)

## Lambda function created by SAM deployment
![lambda](https://user-images.githubusercontent.com/108154106/183280110-8cc98482-3bda-4ad6-a0ba-ff40a225b3e3.png)

## Dynamodb table created by SAM deployment
![dynamodb](https://user-images.githubusercontent.com/108154106/183280121-3ba9b12d-70d4-43af-9bbd-95cecc52fbb6.png)

## SNS topic manually created
![sns](https://user-images.githubusercontent.com/108154106/183280140-ca6c1dba-7d4b-4603-8d92-2a263c7b360f.png)

