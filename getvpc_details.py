import boto3

access = os.environ.get("access", "")
secret = os.environ.get("secret", "")
print(os.environ)
client = boto3.resource(
    'ec2', 
    aws_access_key_id=access,
    aws_secret_access_key=secret,
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

response = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])


print('Route Tables in VPC', vpc_id)
for route_table in response['RouteTables']:
    route_table_id = route_table['RouteTableId']

    # Fetch route table tags to get the name
    tags_response = ec2.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [route_table_id]}])
    tags = {tag['Key']: tag['Value'] for tag in tags_response['Tags']}

    route_table_name = tags.get('Name', 'N/A')
    
    print('Route Table ID:', route_table_id)
    print('Route Table Name:', route_table_name)
    print('==========================')


subnet_associations = response['RouteTables'][0]['Associations']


print('##################################')
for association in subnet_associations:
    subnet_id = association.get('SubnetId')
    # Retrieve subnet information
    subnet_response = ec2.describe_subnets(SubnetIds=[subnet_id])
    subnet_info = subnet_response['Subnets'][0]
    subnet_name = subnet_info.get('Tags', [{'Key': 'Name', 'Value': 'N/A'}])[0].get('Value', 'N/A')
    print('Subnet ID:', subnet_id)
    print('Subnet Name:', subnet_name)
    print('==========================')