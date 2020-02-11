import boto3
from botocore.client import client
import zipfile
import mimetypes

s3 = boto3.resource('s3', config= Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('portfoliobuild.hannah.info')
portfolio_zip = StringIO.StringIO()
build_bucketdownload_fileobj('portfoliobuild.zip', portfolio.zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
with zipfile.ZipFile (portfolio_zip) as myzip: 
     for nm in myzip.namelist(): 
        obj = myzi.open(nm)
        portfolio_bucket.upload_fileobj(obj,nm,
        ExtraArgs={'contentType': mimetypes.guess_type(nm)[0]})
        portfolio_bucket.Object(nm).Acl(put)(ACL='public-read')
        
