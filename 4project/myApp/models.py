from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class login(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   
   picture = models.ImageField(upload_to='images/', default='images/initial.jpeg')
   last_name = models.CharField(max_length=100) #自分の名前（本名)
   first_name = models.CharField(max_length=100)
  
   birth = models.CharField(max_length=8) #生年月日
   school_name = models.CharField(max_length=50) #大学名
   school_major = models.CharField(max_length=1, choices=[('1','文系（教育、美術、言語、文学、音楽、心理学）'),('2', '社会・法学系（国際、法律、政治、社会学）'),('3','会計学・ビジネス・経済学・財政学・マーケティング・貿易'), ('4','科学（農業、コンピュータ・サイエンス、数学、物理学、統計学）'),('5','保険・医療（医学、看護、薬学、公衆衛生）'),('6','工学・建築'),('7','その他')]) #専攻
   school_grade = models.CharField(max_length=1, choices=[('1','1年生'),('2', '2年生'),('3','3年生'), ('4','4年生'),('5','大学院生')]) #学年
   sexuality = models.CharField(max_length=5, choices=[('男','男'),('女', '女'),('その他','その他')])#性別
   insta_ID = models.CharField(max_length=50, null=True, blank=True) #インスタのアカウント名
   twitter_ID = models.CharField(max_length=50, null=True, blank=True) #Twitterのアカウント名
   SNS_name1 = models.CharField(max_length=50, null=True, blank=True) #その他SNSの種類
   SNS_ID1 = models.CharField(max_length=50, null=True, blank=True) #その他SNSのアカウント名
   SNS_name2 = models.CharField(max_length=50, null=True, blank=True) #その他SNSの種類
   SNS_ID2 = models.CharField(max_length=50, null=True, blank=True) #その他SNSのアカウント名

   def __str__(self):
        return self.user.username


class hobby(models.Model):
   login_user = models.ForeignKey(login,on_delete=models.CASCADE)
   hobby1=models.CharField(max_length=5, choices=[('スポーツ','スポーツ'),('読書','読書'),('旅行','旅行'),('カメラ','カメラ'),('映画鑑賞','映画鑑賞')])
   hobby2=models.CharField(max_length=5, choices=[('スポーツ','スポーツ'),('読書','読書'),('旅行','旅行'),('カメラ','カメラ'),('映画鑑賞','映画鑑賞')], null=True, blank=True)
   hobby3=models.CharField(max_length=5, choices=[('スポーツ','スポーツ'),('読書','読書'),('旅行','旅行'),('カメラ','カメラ'),('映画鑑賞','映画鑑賞')], null=True, blank=True)

   def __str__(self):
      return self.login_user.user.username
   

class UserDetail(models.Model):
   #外部キー
   login_user = models.OneToOneField(login, on_delete=models.CASCADE)
   photo1 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   photo2 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   photo3 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   photo4 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   photo5 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   photo6 = models.ImageField(upload_to='photos/', default='photos/photo_initial.jpeg')
   heart = models.BooleanField(default=False)
   profile_text = models.TextField(null=True, blank=True)
   
   def __str__(self):
        return self.login_user.user.username
   

class question(models.Model):
   
   user = models.OneToOneField(login, on_delete=models.CASCADE)
   q1 = models.IntegerField(null=False,blank=False)
   q2 = models.IntegerField(null=False,blank=False)
   q3 = models.IntegerField(null=False,blank=False)
   q4 = models.IntegerField(null=False,blank=False)
   q5 = models.IntegerField(null=False,blank=False)
   q6 = models.IntegerField(null=False,blank=False)
   q7 = models.IntegerField(null=False,blank=False)
   q8 = models.IntegerField(null=False,blank=False)
   q9 = models.IntegerField(null=False,blank=False)
   q10 = models.IntegerField(null=False,blank=False)
   def __str__(self):
        return self.user.user.username
   def publish(self):
        self.save()

class personal(models.Model):
   user = models.OneToOneField(login, on_delete=models.CASCADE)
   diplomacy = models.IntegerField(null=False,blank=False)
   cooperation = models.IntegerField(null=False,blank=False)
   honesty = models.IntegerField(null=False,blank=False)
   nerve = models.IntegerField(null=False,blank=False)
   openness = models.IntegerField(null=False,blank=False)
   
   def __str__(self):
        return self.user.user.username
     
   def publish(self):
      self.save()
   

class Heart(models.Model):
   login_user = models.ForeignKey(login,on_delete=models.CASCADE, related_name='login_user')
   heart_user = models.ForeignKey(login,on_delete=models.CASCADE, related_name='heart_user')

   def __str__(self):
        return self.login_user.user.username
