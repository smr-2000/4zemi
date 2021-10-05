from django import forms
from .models import login
from .models import UserDetail
from .models import hobby
from .models import personal
from .models import question
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

class personalForm(forms.ModelForm):
   class Meta:
      model = question
      fields = (
         'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10'
         )
      data=[
         ('0', '0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
      ]
      data2=[
         ('0', '0'), ('1', '1'),('2', '2'),('3', '3'), ('4', '4'),
      ]
      data3=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data4=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data5=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data6=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data7=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data8=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data9=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      data10=[
         ('0', '0'),('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),
      ]
      choice = forms.ChoiceField(label='初対面の人に会うのが好きで、初対面でも相手との会話を楽しむことができる',choices=data, widget=forms.RadioSelect())
      choice2 = forms.ChoiceField(label='他人に思いやりがあり、それを行動に移してみんなに差別なく親切にできている',choices=data2, widget=forms.RadioSelect())
      choice3 = forms.ChoiceField(label='事をきっちりこなし、手際良く効率よく行っている',choices=data2, widget=forms.RadioSelect())
      choice4 = forms.ChoiceField(label='いつも心配事が多く、不安になりやすい',choices=data2, widget=forms.RadioSelect())
      choice5 = forms.ChoiceField(label='新しいことを知ることが好きで、クリエイティビティが高く好奇心や探究心が強い',choices=data2, widget=forms.RadioSelect())
      choice6 = forms.ChoiceField(label='恥ずかしがり屋で物静かなタイプ',choices=data2, widget=forms.RadioSelect())
      choice7 = forms.ChoiceField(label='思ったことをすぐに口に出し、他人の感情に流されず冷静な判断をする',choices=data2, widget=forms.RadioSelect())
      choice8 = forms.ChoiceField(label='後先考えずに行動して、ぎりぎりまで物事に手をつけない衝動的部分がある',choices=data2, widget=forms.RadioSelect())
      choice9 = forms.ChoiceField(label='大体リラックスして落ち着いている',choices=data2, widget=forms.RadioSelect())
      choice10 = forms.ChoiceField(label='物事を現実的に考え、常識破りなことはしない、割と保守的な考え方である',choices=data2, widget=forms.RadioSelect())
