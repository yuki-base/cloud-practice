# Cloud Practice

AWSとPythonを用いたクラウド学習の記録です。

## 概要

AWS SAAの学習と並行して、Python（boto3）を利用したクラウド運用・監視ツールの開発を行っています。

## 作成したツール

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

### AWS Lambda EC2 Monitor

`lambda_function.py`

AWS Lambda上でPython（boto3）を実行し、EC2インスタンス情報を取得するサーバーレス監視ツール。

## AWS Monitoring Architecture

```text
                +------------------+
                |   EventBridge    |
                | (5分ごと実行)     |
                +--------+---------+
                         |
                         v
                +------------------+
                |      Lambda      |
                |  Python(boto3)   |
                +--------+---------+
                         |
                         v
                +------------------+
                |       EC2        |
                |    test-ec2      |
                +------------------+


                +------------------+
                |   CloudWatch     |
                |  CPU監視         |
                +--------+---------+
                         |
                         v
                +------------------+
                |       SNS        |
                | メール通知        |
                +--------+---------+
                         |
                         v
                +------------------+
                |      Email       |
                +------------------+
```


### 実装内容

* CloudWatchアラームによるCPU使用率監視
* SNSによるメール通知
* EventBridgeによる定期実行
* Lambdaによるサーバーレス監視処理
* EC2インスタンス情報取得

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
* AWS Lambda
* AWS EventBridge
* AWS SNS
* AWS CLI
* Python
* boto3
* Git
* GitHub

## 学んだこと

* IAMによる権限管理
* boto3を利用したAWS操作
* CloudWatchによる監視
* Lambdaを利用したサーバーレス実行
* EventBridgeによる自動実行
* SNSによる通知システム
* Git/GitHubによるソースコード管理

## 今後の予定

* LambdaとCloudWatchの連携強化
* AWS自動化ツール開発
* サーバーレスアーキテクチャ学習

```
```
