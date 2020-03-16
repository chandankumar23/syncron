import boto3

def lambda_handler(event, context):
    client=boto3.resource('dynamodb', region_name='us-east-1')
    table=client.Table('rds_test')
    i=event['i']
    resp=table.get_item(
        Key={
            "InstanceType":i
        })
    return ((resp)['Item'])
