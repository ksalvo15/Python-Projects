# python 3.11.2
# author me
# purpose: to try out a python game 
#
#
#
#
#
#
#


def start(nice=0,mean=0,name=""):

   name = describe_game(name)
   nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
     defining the descripbe_game function   
    """

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
               #asks the player to input their name
                name = input("\nWhat is your name? \n>>>").capitalize()
                #will put in the welcome message if they have put in a name
                if name != "":
                    print("\nWelcome,{}!".format(name))
                    print("\nin this game you will be greeted by severaln\ different people.n\you can choose to be nice or mean")
                    print("\nbut at the end of the game your fate will be revealed by your actions")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nthe stranger approaches you for a \nconversation. will you be nice \nor mean? (N/M) \n>>>:").lower()
        if pick == "n":
            print("\nthe stranger walks away smiling")
            #if they pick nice it will add 1 to the counter
            nice = (nice +1)
            stop = False
        if pick == "m":
            print("\nthe stranger glares at you\n and storms off...")
            #if they pick mean it will add 1 to the counter
            mean = (mean +1)
            stop = False
    score(nice,mean,name)

def show_score(nice,mean,name):
   #shows the total
    print("\n{}, your current total is: \n({}, Nice), and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
#the win or lose conditions of the game
    if nice > 2:
        win(nice,mean,name)
    if mean >2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nnice job {}, you win! \neveryone loves you and you have made \nlots of friends".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nTOO BAD YOU LOSE AND YOU HAVE NO FRIENDS".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\ndo you want to play again? (y/n)\n>>> ").lower()
        if choice =="y":
            stop =False
            reset(nice,mean,name)
        if choice == "n":
            print("\noh so sad sorry to se you go")
            stop = False
            quit()
        else:
            print("\nenter (Y) for 'yes', (N) for 'no':\n>>>")


                       

def reset(nice,mean,name):
    nice = 0
    mean = 0

    start(nice,mean,name)

        


if __name__ == "__main__":
    start()
