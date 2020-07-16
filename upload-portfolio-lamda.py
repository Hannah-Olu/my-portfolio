import boto3
import zipfile
import mimetypes
import StringIO
import mimetypes


def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic(
        'arn:aws:sns:us-east-1:524157238605:deployPortfolioTopic')
    location = {
        "bucketName": "codebuild.clouddevotee2.com",
        "objectKey": "clouddevoteebuild.zip"
    }
    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "BuildArtifact":
                    location = artifact["location"]["s3Location"]

        print("Building portfolio from " + str(location))

        s3 = boto3.resource('s3')
        portfolio_bucket = s3.Bucket('build.clouddevotee.com')
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = StringIO.StringIO()
        print("Location ObjectKey", build_bucket)
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm)
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print("Job done!")
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio deployed successfully!")
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])

    except Exception as e:
        print("Exception: ", e)
        topic.publish(Subject="Portfolio Deploy Failed", Message="The portfolio was not deployed successfully")
    return 'Job done!!'