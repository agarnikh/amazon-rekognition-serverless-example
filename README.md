# Rekognition Serverless Example
This is an Image detection app that uses Rekognition APIs to detect labels S3 Objects, stores labels in DynamoDB and sends SNS notification.
This solution requires to create SNS topic manually and update the ARN of SNS topic to the src/app.py file

## Architecture
<img width="593" alt="architecture" src="https://user-images.githubusercontent.com/108154106/183311042-79dea1c1-7f77-42d6-a91b-6b9ce57713a0.png">


At a high level, the solution architecture use AWS Rekognition service for image analysis:      
   https://aws.amazon.com/rekognition/                        
   https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html          
   https://docs.aws.amazon.com/rekognition/latest/dg/images-information.html         

Following steps are included:
  1. Sets up an Amazon S3 source bucket to storing image.
  2. Configures S3 event notification rule to auto detect a new image upload and call lambda function.
  3. Call Rekognition API to extract image data
  4. Configure DynamoDB table to store image informatiom
  5. Configure SNS topic and subscribe to receive notification upon retrieving and storing data in DynamoDB.

## Prerequisites
 SAM - https://aws.amazon.com/serverless/sam/        
 Cloud9 - https://aws.amazon.com/cloud9/         
 Python upgrade to 3.9 - https://www.gcptutorials.com/post/python3.9-installation-on-amazon-linux-2


## Project structure
Here is a code overview:
```bash
.
├── src                         <-- Source code for the Lambda function
│   ├── __init__.py
│   └── app.py                  <-- Lambda function code
├── template.yaml               <-- SAM template
└── Event.json                  <-- Sample S3 event
```


## Deployment using SAM
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

## 1. S3 Bucket created by SAM deployment
![s3](https://user-images.githubusercontent.com/108154106/183280089-558f0b52-6ebc-48f4-b43c-f6f7444cea30.png)

## 2. Lambda function created by SAM deployment
![lambda](https://user-images.githubusercontent.com/108154106/183280110-8cc98482-3bda-4ad6-a0ba-ff40a225b3e3.png)

## 3. Dynamodb table created by SAM deployment
![dynamodb](https://user-images.githubusercontent.com/108154106/183280121-3ba9b12d-70d4-43af-9bbd-95cecc52fbb6.png)

## 4. SNS topic manually created
![sns](https://user-images.githubusercontent.com/108154106/183280140-ca6c1dba-7d4b-4603-8d92-2a263c7b360f.png)


## Clean up
Deleting the CloudFormation Stack will remove the Lambda functions and other resources created by this solution. 
sam delete command can be used to delete stack.

## Additional sample code
dynamodb_event_reader contains SAM code to deploy DynamoDB table that stream data and check on CloudWatch logs

## License
This library is licensed under the MIT-0 License. See the https://github.com/agarnikh/amazon-Rekognition-serverless-example/blob/main/LICENSE file.
