import boto3 

regions= [
    #'ap-east-1',
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-south-1',
    'ap-southeast-1',
    'ap-southeast-2',
    'ca-central-1',
    'eu-central-1',
    'eu-north-1',
    'eu-west-1',
    'eu-west-2',
    'eu-west-3',
    #'me-south-1',
    'sa-east-1',
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2'
]
for region_name in regions:
    ec2 = boto3.resource('ec2', 
    aws_access_key_id='AKIA4NDHYX54CHRNEU5O',
    aws_secret_access_key='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',
    region_name=region_name)
    instances= ec2.meta.client.describe_instances()
    for instance in instances['Reservations']:
        print(instance['Instances'][0]['InstanceId'], instance['Instances'][0]['State']['Name'])