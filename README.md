# Comprehend serverless Example
This is an Image detection app that uses Rekognition APIs to detect text in S3 Objects, stores labels in DynamoDB and sends SNS topic.
Person need to create the SNS topic manually and add the ARN to src/app.py file

## Requirements
This code need minimum Python 3.9 version

## Design Diagram


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

The `sam deploy` command will create a Cloudformation Stack and deploy your SAM resources.
```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name aws_sam_ocr \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides MyParameterSample=MySampleValue
```

To see the names of the S3 bucket and DynamoDB table created after deployment, you can use the `aws cloudformation describe-stacks` command.
```bash
aws cloudformation describe-stacks \
    --stack-name aws_sam_ocr --query 'Stacks[].Outputs'
```
