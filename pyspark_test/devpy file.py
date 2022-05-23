import datetime as dt
today = dt.date.today()
print(today)
print("dev branch")
print("just test")
import boto3
ACCESS_KEY = "AKIAZQHZB43JDXIAVOVY"
SECRET_KEY = "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"
s3= boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'
# object = s3.Object('my-bucket-rams-faisal1', 'test_file.txt')
# result = object.put(Body=txt_data)
lst = ["This is a test file","123456"]
import pandas as pd
csv_file = pd.read_csv(r'/home/faisal/Downloads/business-financial-data-september-2021-quarter/business-financial-data-sep-2021-quarter.csv')
for i in csv_file.iteritems():
    print(i)
    s3.put_object(Body=i,Bucket='my-bucket-rams-faisal1',Key='test_file.txt')
# print(csv_file.head(5))
# for i in lst:
#     s3.put_object(Body=i,Bucket='my-bucket-rams-faisal1',Key='test_file.txt')