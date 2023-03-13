from jinja2.views import *
from django.urls import path
app_name='shirisha'
urlpatterns=[
    path('specific_jinja/',specific_jinja,name='specific_jinja'),
]