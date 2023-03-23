#people at a university
class university_user:
    University_name = 'Portland State'
    email_format = 'fnamelname@portlandstate.edu'
    fname = ''
    lname = ''
    year =''
    Teacher =''
    building =''
    classes = ''

    def information(self):
        msg = "\nUniversity: {}\nEmail Format: {}\nFirst Name: {}\nLast Name: {}\nyear: {}\nTeacher: {}\nbuilding: {}\nclasses: {}".format(self.University_name,self.email_format,self.fname,self.lname,self.year,self.Teacher,self.building,self.classes)
        return msg
      
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
    teacher = True






if __name__=="__main__":

    student1 = student()
    print(student1.information())
    print(student1.dorms())
        
        
    
