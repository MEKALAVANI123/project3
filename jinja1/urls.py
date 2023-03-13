from jinja1.views import *
from django.urls import path
app_name='shiri'
urlpatterns=[
    path('specific_jinja/',specific_jinja,name='specific_jinja'),
    
]