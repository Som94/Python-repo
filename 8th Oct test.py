
import pandas as pd
dic={'sachin':50,'chetan':80,'leela':90,'nishant':70,'saranya':60,'parvati':75}
df=pd.DataFrame(dic.items(),columns=['name','marks'])
print(df)

print(50*'_')
'''
df['grade']=df['marks'].apply(lambda x : 'a' if x>=90 else 'c')
print(df)
'''

df.loc[(df['marks']>=90), 'grade']='a'
df.loc[(df['marks']>=80) & (df['marks']<90) , 'grade']='b'
df.loc[(df['marks']>=70) & (df['marks']<80) , 'grade']='c'

print(df)

print(50*'_')
filt1=df['grade'].isin(['a','b','c'])

print(df[filt1])

print(50*'_')

filt=df['marks']>70
print(df[filt])
