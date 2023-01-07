from django.shortcuts import render

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "{0} [{1}]".format(self.email, self.password)

# Create your views here.
