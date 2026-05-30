import boto3
from datetime import datetime, timedelta, timezone

cloudwatch = boto3.client("cloudwatch")

instance_id = "i-0742c55e8483b4d45"

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(minutes=30)

response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[
        {
            "Name": "InstanceId",
            "Value": instance_id
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average"]
)

print("=== EC2 CPU使用率 ===")

datapoints = response["Datapoints"]

if datapoints:
    for point in datapoints:
        print(point["Timestamp"], point["Average"])
else:
    print("データなし")