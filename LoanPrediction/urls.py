from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welcome, name='welcome'),
    path('forminfo',views.formInfo, name='forminfo'),
    path('predict',views.predict, name='predict')
]
