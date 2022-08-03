import email
import uuid
from django.db import models
from django.forms import BooleanField
from django.utils import timezone

# Create your models here.

class user(models.Model):
    uuid=models.AutoField(primary_key=True,editable=False)
    email=models.EmailField()
    name=models.CharField(max_length=200,null=True,blank=True)
    encrypted_password=models.CharField(max_length=200,null=False,blank=False)
    reset_password_token=models.CharField(max_length=200,null=False,blank=False)
    reset_password_sent_at = models.DateTimeField(auto_now_add=True)
    remember_created_at =  models.DateTimeField(auto_now_add=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    sign_in_count=models.IntegerField(default=0)
    current_sign_in_at =  models.DateTimeField(auto_now=True)
    last_sign_in_at =  models.DateTimeField(auto_now=True)
    current_sign_in_ip = models.GenericIPAddressField()
    last_sign_in_ip =  models.GenericIPAddressField()
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    affiliate_id = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    confirmation_token = models.CharField(max_length=200,null=True,blank=True)
    confirmed_at = models.DateTimeField(auto_now_add=True)
    confirmation_sent_a = models.DateTimeField(auto_now_add=True)
    unconfirmed_emai = models.EmailField()
    failed_attempts = models.IntegerField(default=0)
    locked_at = models.DateTimeField(auto_now=True)
    email_confirmed = BooleanField(default = False,null = False,blank=False)
    unconfirmed_email_request = BooleanField(default = False,null = False,blank=False)
    kyc_status =  models.CharField(max_length=200,null=False,blank=False,default='not_completed')
    banned_reason =  models.CharField(max_length=200,null=True,blank=True)   
    banned = BooleanField(default = False,null = False,blank=False)
    kyc_status_reason = models.CharField(max_length=200,null=True,blank=True)
    affiliate_status = models.CharField(max_length=200,null=True,blank=True, default='not_completed')
    affiliate_formed_id = models.CharField(max_length=200,null=True,blank=True)






