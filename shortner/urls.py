from django.urls import path
from . import views


# path: This is a function provided by Django for defining URL patterns. It is used to map a URL pattern to a specific view function.
# '/<str:nik>': This is the URL pattern itself, which contains a variable part <str:nik>. 
# The <str:nik> syntax indicates that this part of the URL is a string parameter named "nik" 
# The angle brackets < > are used to capture the value from the URL 
# and pass it as a keyword argument to the associated view function.
urlpatterns = [
    path('',views.index, name='index'),
    path('create',views.create,name='create'),
    path('<str:nik>',views.visit,name='visit')
]
