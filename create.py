import boto3
import base64
import os
access = os.environ.get("access", "")
secret = os.environ.get("secret", "")
print(os.environ)
client = boto3.resource(
    'ec2', 
    aws_access_key_id=access,
    aws_secret_access_key=secret,
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


    