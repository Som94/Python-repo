
import pandas as pd
import configparser
import boto3

config_obj=configparser.ConfigParser()


config_obj.read(r'E:\Aroha Tech\Python Session\awsbucketconfig.ini')
header=config_obj['aws']

bucket=header['Bucket']

s3_resource=boto3.resource('s3')

s3_client=boto3.client('s3')

obj=s3_client.get_object(Bucket=bucket,Key='customer.csv')

df=pd.read_csv(obj['Body'])

