from datetime import datetime       
#global pat_id
pat_dict={}
        
class Patient:
    def setDetails(self,pat_id, pname, pmobile, pemail_id,pdob, pgender, disease):
        self.pat_id = pat_id
        self.pname = pname
        self.pmobile=pmobile
        self.pemail_id=pemail_id
        self.pdob=pdob
        self.pgender=pgender
        self.disease=disease
    def getDetails(self):
        pat_dict[self.pat_id]=(self.pat_id, self.pname, self.pmobile, self.pemail_id,self.pdob, self.pgender, self.disease)
        return pat_dict
    

record_list=[]
class Hospital:
    
    
    doc_dict={1001:(1001,'Rohit',7978840210,"Som@gmail.com",'31/05/1985','male','mbbs','D554','Cadiologist'),
          1002:(1002,'Dhoni',7978844422,"Som@gmail.com",'14/10/1984','male','mbbs','D555','Dermatologists'),
          1003:(1003,'Kohli',9988552100,"Som@gmail.com",'06/07/1985','male','mbbs','D556','Endocrinologists'),
          1004:(1004,'Surya',7852411031,"Som@gmail.com",'31/10/1994','male','mbbs','D557','Urologist')}
    
    def __init__(self,pat_id):
        self.pat_id=pat_id
    def Consultant(self,pat_id):
        
        
        
        if pat_dict[self.pat_id][6]=='Cadiologist':
            record_list.append((1001,pat_id,'probelm on kidney',str(datetime.now())))
        if pat_dict[self.pat_id][6]=='Dermatologists':
            record_list.append((1002,pat_id,'probelm on kidney',str(datetime.now())))
        if pat_dict[self.pat_id][6]=='Endocrinologists':
            record_list.append((1003,pat_id,'probelm on kidney',str(datetime.now())))
        if pat_dict[self.pat_id][6]=='Urologist':
            record_list.append((1004,pat_id,'probelm on kidney',str(datetime.now())))

        
   
    #def PRESCRIPTION:
       # def getPrescription(self,doc_id,pat_id,medicine_name,quantity,days,date):
            
        
        
    #class Transaction:

p=Patient()

p.setDetails(100,'saam',9658755334,'s@gmail.com','12/12/20','female','Urologist')
p.getDetails()



h=Hospital(100)
h.Consultant(100)

print(record_list)


    
    