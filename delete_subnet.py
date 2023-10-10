import boto3
import argparse

parser = argparse.ArgumentParser(description='--description--')
parser.add_argument('--subnet_id', help='subnet_id --description--')
args = parser.parse_args()

subnet_id = None
if args.subnet_id:
    subnet_id = args.subnet_id

access = os.environ.get("access", "")
secret = os.environ.get("secret", "")
print(os.environ)
client = boto3.resource(
    'ec2', 
    aws_access_key_id=access,
    aws_secret_access_key=secret,
    region_name='us-east-1')


response = ec2.delete_subnet(SubnetId=subnet_id)
print('Response from deleting subnet:', response)