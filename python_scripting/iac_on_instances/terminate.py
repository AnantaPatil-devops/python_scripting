import boto3

session = boto3.Session(
    aws_access_key_id = "aws_access_key_id",
    aws_secret_access_key = "aws_secret_access_key",
    region_name='us-east-1'
)

ec2_client = session.client("ec2")
instance_id_to_terminate = input("Enter the instance ID to terminate: ")
response = ec2_client.describe_instances(InstanceIds=[instance_id_to_terminate])

if not response['Reservations']:
    print(f"Instance with ID{instance_id_to_terminate} not found")
else:
    ec2_client.terminate_instances(InstanceIds=[instance_id_to_terminate])
    print(f"Instance with ID{instance_id_to_terminate} is terminated succesfully")
