from django.conf import settings
from django.db import models

class login(models.Model):
   name = models.CharField(max_length=10) #自分の名前（本名)
   password = models.CharField(max_length=8) #パスワード
   mail = models.TextField() #メールアドレス
   birth = models.CharField(max_length=8) #生年月日
   school_name = models.TextField() #大学名
   school_grade = models.CharField(max_length=1) #学年
   sexuality = models.TextField()#性別
   insta_ID = models.TextField() #インスタのアカウント名
   twitter_ID = models.TextField() #Twitterのアカウント名
   SNS_name1 = models.TextField() #その他SNSの種類
   SNS_ID1 = models.TextField() #その他SNSのアカウント名
   SNS_name2 = models.TextField() #その他SNSの種類
   SNS_ID2 = models.TextField() #その他SNSのアカウント名

   def publish(self):
        self.save()

   def __str__(self):
        return self.name
