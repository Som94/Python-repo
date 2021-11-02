import pandas as pd
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='test',user='root',password='root',port=3306)