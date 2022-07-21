    #print(e)
    print(‘STEP 1 - Entering Lambda Handlder!’)
    s3 = boto3.client(‘s3’)
    print(‘STEP 2 - Calling S3 bucket!’)
    bucket = event[‘Records’][0][‘s3’][‘bucket’][‘name’]
    print(bucket)
    print(‘STEP 3 - Fatching the Key!’)
    key = urllib.parse.unquote_plus(event[‘Records’][0][‘s3’][‘object’][‘key’], encoding=‘utf-8’)
    print(key)
    print(‘STEP 4 - Fatching the S3 Object’)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(“CONTENT TYPE: ” + response[‘ContentType’])
        print(‘STEP 5 - Completed S3 bucket operation!’)
        #return response[‘ContentType’]
        client1 = boto3.client(‘textract’)
        print(‘STEP 6 - Configured TextRact!’)
        response1 = client1.analyze_id(DocumentPages=[{‘S3Object’: {‘Bucket’: bucket, ‘Name’: key}}])
        print(‘STEP 7 - Got response from TextRact!’)
        print(‘STEP 8 - Writing to DynamoDB!’)
        client2 = boto3.client(‘dynamodb’)
        data2 = client2.put_item(TableName=‘licenseid’, Item={
            ‘ID’: {
            #‘S’: ‘JASON’
            ‘S’: response1.IdentityDocuments[0].IdentityDocumentFields[0].ValueDetection.Text
            }}
        )
        print(‘STEP 9 - Sending SNS Notification!’)
        notification = “Here is the SNS notification for Lambda function tutorial.”
        client5 = boto3.client(‘sns’)
        response5 = client5.publish (
            TargetArn = “arn:aws:sns:us-west-1:468885651811:licensetopic”,
           Message = json.dumps({‘default’: notification}),
            MessageStructure = ‘json’
        )
        print(response1)
    except Exception as e:
        print(e)
        print(‘Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.’.format(key, bucket))
        raise e
    print(‘About to return1!’)
    return {
        “statusCode”: 200,
        “body”: json.dumps({
            “message”: “Image added to DynamoDB and SNS notificastion sent”,
            # “location”: ip.text.replace(“\n”, “”)
        }),
    }
    
    */