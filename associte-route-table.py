import boto3

def create_subnet_associate_route_table(vpc_id, cidr_block, route_table_id):
    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Create subnet
    subnet_response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr_block
    )

    subnet_id = subnet_response['Subnet']['SubnetId']
    print('Subnet created with ID:', subnet_id)

    # Associate subnet with route table
    ec2.associate_route_table(
        SubnetId=subnet_id,
        RouteTableId=route_table_id
    )

    print('Subnet associated with Route Table:', route_table_id)

# Replace these with your actual values
vpc_id = 'YOUR_VPC_ID'
cidr_block = '10.0.0.0/24'
route_table_id = 'YOUR_ROUTE_TABLE_ID'

create_subnet_associate_route_table(vpc_id, cidr_block, route_table_id)
