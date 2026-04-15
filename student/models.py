from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_num=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=254)
    address=models.TextField()
    def __str__(self):
        return self.name
    

