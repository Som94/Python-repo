
import configparser

config=configparser.ConfigParser()

config.add_section('mysql')
config.set('mysql','host','localhost')
config.set('mysql','user','root')
config.set('mysql','password','root')
config.set('mysql','port','3306')
config.set('mysql','db','test')

with open(r'E:\Aroha Tech\Python Session\mysqwldbconfig.ini','w') as  configfile:
    config.write(configfile)