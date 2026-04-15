from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('student/<int:id>/',views.std_detail),
    path('addstudent/',views.add_std,name='add_std'),

]