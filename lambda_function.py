import boto3

def lambda_handler(event, context):

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })

    return {
        "statusCode": 200,
        "body": instances
    }