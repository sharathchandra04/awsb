import boto3
import argparse

#public subnet and private subnet using the arg parser.

parser = argparse.ArgumentParser(description='--description--')
parser.add_argument('--cidr', help='subnet_cidr_block --description--')
parser.add_argument('--name', help='subnet_cidr_block --description--')
args = parser.parse_args()

subnet_cidr_block = None
name = None
if args.cidr:
    subnet_cidr_block = args.cidr
if args.cidr:
    name = args.name

access = os.environ.get("access", "")
secret = os.environ.get("secret", "")
print(os.environ)
client = boto3.resource(
    'ec2', 
    aws_access_key_id=access,
    aws_secret_access_key=secret,
    region_name='us-east-1')



vpc_id = 'vpc-0c34260e2a53009e3'

# subnet_cidr_block = '10.25.6.0/24'
availability_zone = 'us-east-1a'


response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock=subnet_cidr_block,
    AvailabilityZone=availability_zone,
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': name
                }
            ]
        }
    ]
)
print('Subnet ID:', response['Subnet']['SubnetId'])

route_table_id = 'YOUR_ROUTE_TABLE_ID'
association_response = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=response['Subnet']['SubnetId']
)

print('Route table associated with subnet:', association_response['AssociationId'])

