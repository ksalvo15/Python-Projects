#people at a university
class university_user:
    University_name = 'Portland State'
    fname = ''
    lname = ''
    email_format = '{}{}@portlandstate.edu'.format(fname,lname) #need to fix this for later
    year =''
    Teacher =''
    building =''
    classes = ''
    password = 'password1234'

    def information(self):
        msg = "\nUniversity: {}\nFirst Name: {}\nLast Name: {}\nEmail Format: {}\nyear: {}\nTeacher: {}\nbuilding: {}\nclasses: {}".format\
              (self.University_name,self.fname,self.lname,self.email_format,self.year,self.Teacher,self.building,self.classes)
        return msg

    def login(self):
        #has the user enter in information
        user_name = input("enter your username")
        user_email = input("enter your email")
        user_password = input("enter your password")
        if (user_email ==self.email_format and user_password ==self.password):
            print("welcome back {}".format(user_name))
            #adds a message if the input is wrong
        else:
            print("the user email or password is incorrect")
      
#students at a university
class student(university_user):
    fname = 'jane'
    lname = 'smith'
    classes = 'Math'
    year = 'Sopomore'
    Teacher = False

    def dorms(self):
        msg = "they are a student here"
        return msg

#teachers at a university
class teacher(university_user):
    building = 'Building A'
    fname = 'Bill'
    lname = 'smith'
    email_format = 'billsmith@portlandstate.edu'
    teacher = True
    pin = '1234'

#the information asked for is slightly different if they are a teacher
    def login(self):
        user_name = input("enter your username")
        user_email = input("enter your email")
        user_pin = input("enter your teacher pin")
        if (user_email ==self.email_format and user_pin ==self.pin):
            print("welcome back {}".format(user_name))
        else:
            print("the user email or pin is incorrect")




if __name__=="__main__":

    student1 = student()
    print(student1.information())
    print(student1.dorms())

    teachers= teacher()
    teachers.login()
    
    students = university_user()
    students.login()
        
        
    
