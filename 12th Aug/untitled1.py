class A:   

    def stNe(self,name):
        self.name = name
        
    def gtNme(self):
        
        return self.name
a=A()
a.stNe(1000)
b=a.gtNme()
print(b)


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
        

for i in range(2):
    p=Patient()
    p.setDetails(100,'saam',9658755334,'s@gmail.com','12/12/20','female','None')
    p.getDetails()
    p.setDetails(100,'sm',9658755334,'s@gmail.com','12/12/20','female','None')
    p.getDetails()
print(pat_dict[100][4])
