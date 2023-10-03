import boto3

# Initialize the Boto3 EC2 client
# ec2 = boto3.client('ec2')

ec2 = boto3.client(
    'ec2', 
    aws_access_key_id='AKIA4NDHYX54CHRNEU5O',
    aws_secret_access_key='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',
    region_name='us-east-1')

# Specify the VPC ID
vpc_id = 'vpc-0c34260e2a53009e3'

# Get details of the specified VPC
response = ec2.describe_vpcs(VpcIds=[vpc_id])

# Print VPC details
vpc_details = response['Vpcs'][0] if 'Vpcs' in response else None
if vpc_details:
    print('VPC ID:', vpc_details['VpcId'])
    print('CIDR Block:', vpc_details['CidrBlock'])
    print('State:', vpc_details['State'])
    print('Tags:', vpc_details.get('Tags', 'N/A'))
else:
    print('VPC not found or no VPCs returned.')


sn_response = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])

print('\n##### subnets details')
subnets = sn_response['Subnets'] if 'Subnets' in sn_response else []
if subnets:
    print('Subnets associated with VPC ID', vpc_id)
    for subnet in subnets:
        print('Subnet ID:', subnet['SubnetId'])
        print('CIDR Block:', subnet['CidrBlock'])
        print('Availability Zone:', subnet['AvailabilityZone'])
        print('Tags:', subnet.get('Tags', 'N/A'))
        print()
else:
    print('No subnets found for the specified VPC.')
