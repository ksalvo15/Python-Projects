from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


#this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # gets the transaction form
    # checks to see if the request method is post
    if request.method == 'POST':
        pk = request.POST['account'] # if the form is submitted then it will grab the user with the pk key the user wants
        return balance(request, pk)  # call balance function to render the accounts balance sheet
    content = {'form': form}
    # adds content of form to the page
    return render(request, 'checkbook/index.html', content)


#this function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #gets the account form
    #checks to see if the request method is post
    if request.method == 'POST':
        if form.is_valid(): #checks if the form is submitted and valid
            form.save() #if it is then saves
            return redirect('index') #takes user to the home page afer submission
    content = {'form': form}
    #adds content of form to the page
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retrieve the requested account using it's pk
    transactions = Transaction.Transactions.filter(account=pk) #retreieves all of that accounts transactions
    current_total = account.initial_deposit #create account total variable strating with the intial deposit value
    table_contents = {} #create a dictionary itno which transaction information will be placed
    for t in transactions: #loop through transactions and determine which is a depositt of withdrawl
        if t.type =='Deposit':
            current_total+=t.amount #if its a deposit add it to balance
            table_contents.update({t: current_total}) #adds transaction and total to the dictionary
        else:
            current_total -= t.amount #if withdrawl subtract
            table_contents.update({t: current_total})
    # pass account account toal and the transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None) #gets the transaction form
    # checks to see if the request method is post
    if request.method == 'POST':
        if form.is_valid(): #checks if the form is submitted and valid
            pk = request.POST['account']#retreieves the account for the trnsaction
            form.save() #if it is then saves
            return balance(request, pk) #renders the balance
    content = {'form': form}
    # adds content of form to the page
    return render(request, 'checkbook/AddTransaction.html', content)
