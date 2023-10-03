import boto3
import argparse

parser = argparse.ArgumentParser(description='--description--')
parser.add_argument('--subnet_id', help='subnet_id --description--')
args = parser.parse_args()

subnet_id = None
if args.subnet_id:
    subnet_id = args.subnet_id

ec2 = boto3.client(
    'ec2', 
    aws_access_key_id='AKIA4NDHYX54CHRNEU5O',
    aws_secret_access_key='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',
    region_name='us-east-1')

response = ec2.delete_subnet(SubnetId=subnet_id)
print('Response from deleting subnet:', response)