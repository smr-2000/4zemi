from django import forms
from .models import login

class UserForm(forms.ModelForm):
   class Meta:
       model = login
       fields = (
          'picture',
          'name',
          'password',
          'mail',
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
          'name':'名前*',
          'password':'パスワード*',
          'mail':'メールアドレス*',
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
      
