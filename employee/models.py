from django.db import models

class Employee(models.Model):
    fnames =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    phone =models.IntegerField()
    addres =models.CharField(max_length=200)
    created_at =models.DateTimeField(auto_now_add=True)
    
        