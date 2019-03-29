from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$',views.landing,name='landing'),
    url(r'home',views.home,name='home'),
    url(r'wallet',views.wallet,name='wallet'),
    url(r'savings',views.savings,name='savings'),
    url(r'addsave',views.addsave,name='addsave'),
    url(r'finance',views.finance,name='finance'),
]
