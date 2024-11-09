from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Income(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)
    source = models.CharField(max_length=100)
    description = models.TextField()
    receipt = models.ImageField(upload_to='receipts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.source
    
    # lets create a class meta to order the expenses by the date
    class Meta:
        ordering = ['-date']

    # let define the class category to return the category in a list
class UserSource(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 

        