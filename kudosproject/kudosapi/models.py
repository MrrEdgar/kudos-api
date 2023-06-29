from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)

class User(models.Model):
    fullname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Kudos(models.Model):
    message = models.CharField(max_length=200)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')


