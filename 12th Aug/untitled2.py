class Hospital:
    def __init__(self,doc_id,Pat_id):
        self.doc_id=doc_id
        self.Pat_id=Pat_id
    def display(self):
        print("DOctor Id :",self.doc_id,"Patient Id :",self.Pat_id)


    class Doctors:
        def __init__(self,doc_id, dname, dmobile, demail_id, ddob, dgender,qualification, regd_number, specialisation):
            self.doc_id = doc_id
            self.dname = dname
            self.dmobile=dmobile
            self.demail_id=demail_id
            self.ddob=ddob
            self.dgender=dgender
            self.qualification=qualification
            self.regd_number=regd_number
            self.specialisation=specialisation
        def display(self):
            print("Doctor Id :",self.doc_id)
            print("Doctor Name :",self.dname)
            print("Doctor Mobile :",self.dmobile)
            print("Doctor Email Id :",self.demail_id)
            print("Doctor DOB :",self.ddob)
            print("Doctor Gender :",self.dgender)
            print("Doctor qualification :",self.qualification)
            print("Doctor regd_number :",self.regd_number)
            print("Doctor specialisation :",self.specialisation)
            
            
h=Hospital(1000,1001)
#h.display()
d=h.Doctors(1000,'Som',9658755334,"Som@gmail.com",'31/10/1994','male','mbbs','D555','Cadiologist')
d.display()

doc_dict={1001:(1000,'Rohit',7978840210,"Som@gmail.com",'31/05/1985','male','mbbs','D554','Cadiologist'),
          1002:(1002,'Dhoni',7978844422,"Som@gmail.com",'14/10/1984','male','mbbs','D555','Dermatologists'),
          1003:(1003,'Kohli',9988552100,"Som@gmail.com",'06/07/1985','male','mbbs','D556','Endocrinologists'),
          1004:(1004,'Surya',7852411031,"Som@gmail.com",'31/10/1994','male','mbbs','D557','Urologist')}


