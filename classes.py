#people at a university
class university_user:
    name = ''
    email = ''
    password = ''
    username = ''

#students at a university
class student(university_user):
    classes = ''
    year = ''

#teachers at a university
class teacher(university_user):
    department = ''
    building = ''
