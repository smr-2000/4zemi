from django import forms
from .models import login
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

class UserForm(forms.ModelForm):
   class Meta:
       model = login
       fields = ('name', 'password', 'mail', 'birth', 'school_name', 'school_grade', 'sexuality')
       labels = {
           'name':'名前',
           'password':'パスワード',
           'mail':'メールアドレス',
           'birth':'生年月日',
           'school_name':'学校名',
           'school_grade':'学年',
           'sexuality':'性別',
       }

class LoginForm(ModelForm):
   class Meta:
      model = login
      fields = ['mail','password']
      
