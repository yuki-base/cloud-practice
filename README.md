# Cloud Practice

AWSとPythonを用いたクラウド学習の記録です。

## 概要

AWS SAAの学習と並行して、Python（boto3）を利用したクラウド運用・監視ツールの開発を行っています。

## 学習内容

### Day3 Linux Permission Study

* Linuxのファイル権限について学習
* chmodによる権限変更を実践

### Day5 IAM Role Verification

* IAMユーザーとIAMロールの違いを学習
* 最小権限の考え方を学習
* Access KeyとIAMロールによる認証を理解

### Day6 AWS Monitoring Practice

* boto3を利用したAWSサービス操作
* EC2監視ツール作成
* CloudWatchによるCPU使用率取得

## Python × AWS

### S3 Bucket List Tool

`s3_list.py`

S3バケット一覧を取得するツール。

### EC2 Instance Status Tool

`ec2_list.py`

EC2インスタンスの名前、ID、状態を取得するツール。

### Stopped EC2 Check Tool

`stopped_ec2_check.py`

停止中のEC2インスタンスを検知するツール。

### EC2 Monitoring Tool

`ec2_monitor.py`

起動中・停止中のEC2インスタンスを分類して表示する監視ツール。

### EC2 CPU Monitoring Tool

`ec2_cpu_check.py`

CloudWatchからEC2のCPU使用率を取得する監視ツール。

## 実行例

### EC2 Monitoring Tool

```text
=== 起動中 ===
test-ec2

=== 停止中 ===
なし
```

### EC2 CPU Monitoring Tool

```text
=== EC2 CPU使用率 ===
0.16%
```

## 使用技術

* AWS IAM
* AWS EC2
* AWS S3
* AWS CloudWatch
* AWS CLI
* Python
* boto3
* Git
* GitHub

## 今後の予定

* AWS Lambda
* CloudWatchアラーム
* AWS自動化ツール開発
* サーバーレスアーキテクチャ学習
