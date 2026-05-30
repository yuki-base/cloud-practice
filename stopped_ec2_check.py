import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

print("=== 停止中EC2 ===")

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        state = instance["State"]["Name"]

        if state == "stopped":

            name = "No Name"

            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]

            print(name)