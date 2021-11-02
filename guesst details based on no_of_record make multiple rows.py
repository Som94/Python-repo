import pandas as pd

guest_details=pd.read_csv(r'E:\Aroha Tech\Data Platform\ETL\guest_details.csv')

print(guest_details)

result_details=pd.DataFrame(columns=['guest_name','city','phone','company','No_of_records'])

for i,row in guest_details.iterrows():
    count=1
    while row.No_of_records >= count:
        result_details=result_details.append(guest_details.iloc[i])
        count=count+1
        
result_details.drop(['No_of_records'],axis=1, inplace=True)

print(result_details)

result_details.to_csv(r'E:\Aroha Tech\Data Platform\ETL\Results_of_guest.csv', index=False, sep=',')
