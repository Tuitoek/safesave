from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    name=models.CharField(max_length=30)
    email=models.EmailField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()

class Month(models.Model):
    months = models.CharField(max_length=30)

    def __str__(self):
        return self.months

class SavingPlan(models.Model):
    amount= models.CharField(max_length=40)
    month = models.ForeignKey(Month)

    def __str__(self):
        return self.amount

class Finance(models.Model):
    user =  models.OneToOneField(User)
    amount = models.CharField(max_length=50,null=True)
    expenses = models.CharField(max_length=100)
    salaryearned = models.CharField(max_length=1000)
    extracash = models.CharField(max_length=100,null=True)
    savings = models.ForeignKey(SavingPlan)
    months = models.ForeignKey(Month)



    def save_finance(self):
        self.save()

    def delete_finance(self):
        self.delete()

    def update_finance(self):
        self.save()
