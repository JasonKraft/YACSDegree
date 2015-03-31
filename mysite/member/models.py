from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)   
    
    def __unicode__(self):
        return self.name
    
    
    
#def create_member_user_callback(sender, instance, **kwargs):
 #   member, new = Member.objects.get_or_create(user=insance)

#post_save.connect(create_member_user_callback, User)