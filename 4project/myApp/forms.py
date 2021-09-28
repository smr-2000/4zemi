from django import forms
from .models import login
from .models import UserDetail
from .models import hobby
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
         'school_major',
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
         'school_major':'専攻*',
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

    
class UserDetailForm(forms.ModelForm):
   class Meta():
      model = UserDetail
      fields = (
         'photo1',
         'photo2',
         'photo3',
         'photo4',
         'photo5',
         'photo6',
         'heart',
         'profile_text',
      )
      labels = {
         'photo1':'画像1',
         'photo2':'画像2',
         'photo3':'画像3',
         'photo4':'画像4',
         'photo5':'画像5',
         'photo6':'画像6',
         'heart':'いいね',
         'profile_text':'プロフィール',
      }
         
class SelectHobby(forms.ModelForm):
   class Meta():
      model = hobby

      fields = (
         'hobby1',
         'hobby2',
         'hobby3',
      )
      labels = {
         'hobby1':'1番好きな趣味*',
         'hobby2':'2番目に好きな趣味',
         'hobby3':'3番目に好きな趣味',
      }
