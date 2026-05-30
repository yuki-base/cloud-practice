import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

running = []
stopped = []

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        state = instance["State"]["Name"]

        name = "No Name"
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]

        if state == "running":
            running.append(name)

        elif state == "stopped":
            stopped.append(name)

print("=== 起動中 ===")
if running:
    for name in running:
        print(name)
else:
    print("なし")

print("\n=== 停止中 ===")
if stopped:
    for name in stopped:
        print(name)
else:
    print("なし")