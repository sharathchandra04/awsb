import boto3
import base64

client = boto3.resource(
    'ec2', 
    aws_access_key_id='AKIA4NDHYX54CHRNEU5O',
    aws_secret_access_key='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',
    region_name='us-east-1')


with open("../docker/docker-install.sh", "rb") as data:
    encoded_string = base64.b64encode(data.read())
    instances = client.create_instances(
            ImageId="ami-053b0d53c279acc90",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="newmalcom",
            UserData=encoded_string,
            SecurityGroupIds=[
                'sg-021bac6a25fe29b94',
            ],
            SubnetId='subnet-0eec18be519daf758',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'docker1'
                        },
                    ]
                },
            ],
        )

    instances[0].wait_until_running()
    instances[0].reload()
    print(instances[0], type(instances[0]))
    private_ip = instances[0].private_ip_address
    public_ip = instances[0].public_ip_address
    print(instances, 'connect --->  ', f'ssh -i "newmalcom.pem" ubuntu@{public_ip}')


    