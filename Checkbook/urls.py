from django.urls import path
from . import views


urlpatterns = [
    #sets url path to the home page index.html
    path('', views.home, name='index'),
    #sets the url path to add a new create page from the html template
    path('create', views.create_account, name='create'),
    #sets the url path to add a new balance page from the html template
    path('balance', views.balance, name='balance'),
    #sets the url path to add a new transaction page from the html template
    path('transaction', views.transaction, name='transaction'),
    #sets the url path to add a new balance page from the html template using the pk
    path('<int:pk>/balance/', views.balance, name='balance'),
]