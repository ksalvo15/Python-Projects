import datetime

import pytz

portland=pytz.timezone('PST')
newyork=pytz.timezone('EST')
london=pytz.timezone('London')

def gettimes(portland,newyork,london):
    currenttime = datetime.datetime.now()
    portlandtime=currenttime.astimezone(portland)
    newyorktime =currenttime.astimezone(newyork)
    londontime =currenttime.astimezone(london)
    return portlandtime, newyorktime, londontime

def compare(portland,newyork,london):
    portlandtime, newyorktime, londontime=gettimes(portland,newyork,london)
    branches = {"Portland": portlandtime, "New York": newyorktime, "London": londontime}
    for branch in branches.keys():
        o=True
        currenthour=int(branches[branch].time().strftime('%H'))
        currenttime=branches[branch].time().strftime('%H:%M')
        if currenthour <9 or currenthour > 17:
            o=False
        if o:
            print("the {} branch is open, the time is {}".format(branch,currenttime))
        else:
            print("the {} branch is closed, the current time is {}".format(branch,currenttime))

compare(portland,newyork,london)




