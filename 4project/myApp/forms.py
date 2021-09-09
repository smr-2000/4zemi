from django import forms
from .models import login
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
   class Meta():
      model = User
      fields = (
         'username',
         'email',
         'password',
      )
      labels = {
         'username':'ユーザー名*',
         'email':'メールアドレス*',
         'password':'パスワード*',
      }

class AddUserForm(forms.ModelForm):
   class Meta():
      model = login
      fields = (
         'picture',
         'last_name',
         'first_name',
         'birth',
         'school_name',
         'school_grade',
         'sexuality',
         'insta_ID',
         'twitter_ID',
         'SNS_name1',
         'SNS_ID1',
         'SNS_name2',
         'SNS_ID2',
      )
      labels = {
         'picture':'プロフィール画像',
         'last_name':'名字',
         'first_name':'名前',
         'birth':'生年月日*',
         'school_name':'学校名*',
         'school_grade':'学年*',
         'sexuality':'性別*',
         'insta_ID':'InstagramのID',
         'twitter_ID':'TwitterのID',
         'SNS_name1':'その他SNSの種類',
         'SNS_ID1':'その他SNSのID',
         'SNS_name2':'その他SNSの種類',
         'SNS_ID2':'その他SNSのID',
      }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
