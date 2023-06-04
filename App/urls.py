from django.urls import path
from . views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('allProf/', allProf, name='allProf'),
    path('createProf/', createProf, name='createProf'),
    path('profView/<int:id>/', profView, name='profView'),
    path('deleteProf/<int:id>/', deleteProf, name='deleteProf'),
    path('update/<int:id>/', update, name='update'),
]
