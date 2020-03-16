# lambda function to insert records to dynamo db. The function once deployed will have to configured to trigger every 5 mins using the cron entry.

import boto3
def lambda_handler(event, context):
    client=boto3.client('rds')
    response=client.describe_db_instances()
    for r in response['DBInstances']:
        db_type=r['DBInstanceClass']
        db_endpoint=r['Endpoint']
        db_endpoint_hostzoneid = db_endpoint["HostedZoneId"]
        db_endpoint_port = db_endpoint["Port"]
        db_endpoint_address = db_endpoint["Address"]
        db_endpoint_2=("%s %s %s" %(db_endpoint_hostzoneid,db_endpoint_port,db_endpoint_address))
        # print db_type
        # print db_endpoint_2
        # print db_endpoint_port
        # print db_endpoint_address
    client = boto3.resource('dynamodb', region_name='us-east-1')
    table = client.Table("syncron_get_rds_info")
    for r in response['DBInstances']:
        table.put_item(
        Item={
        ''
        'Endpoint':db_endpoint_2,
        'InstanceType':db_type
        }
        )

## Steps to trigger lambda every 5 minutes

## Create event with a "rate of 5 minutes"
## aws events put-rule --name "Syncron_insert_dynamo" --schedule-expression "rate 5 minutes"
## Define the targets for the 5 minutes events
## aws events put-targets --rule "Syncron_insert_dynamo" --targets "syncron_insert_dynamo"
