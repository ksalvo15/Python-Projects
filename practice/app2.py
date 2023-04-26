import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
#the following is calling wcod from within the script
    print("i am running code from {}".format(print_app2()))
    
    #the following is calling wcod from outside the script imported app.py
    print("i am running code from {}".format(app.print_app()))
