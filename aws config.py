import configparser

config=configparser.ConfigParser()

config.add_section('aws')
config.set('aws','Bucket','o-sales-etl')


with open(r'E:\Aroha Tech\Python Session\awsbucketconfig.ini','w') as  configfile:
    config.write(configfile)