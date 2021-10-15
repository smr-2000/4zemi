from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import UserForm
from .forms import LoginForm
from .forms import AddUserForm
from .forms import UserDetailForm
from .forms import SelectHobby
from .forms import personalForm
from .forms import HeartForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ページが存在すれば表示、しなければ404エラー
from django.shortcuts import get_object_or_404
from .models import login
from .models import UserDetail
from .models import hobby
from .models import personal
from .models import question
from .models import Heart
import random

# Create your views here.
user_username = "ユーザーネーム"
user_pass = "パスワード"

def new_register(request):
    return render(request, 'myApp/new_register.html', {})


def details_screen(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userdetail = UserDetail.objects.filter(login_user=userinfo)

    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']
    
    user = authenticate(username=user_username, password=user_pass)
    login(request, user)
    
    if userdetail.exists():
        userinfoMypage = userdetail[0]
        
        context = {
            'userinfo':userinfo,
            'userinfoMypage':userinfoMypage,
            'user_username':user_username,
            'user':user,
        }
        return render(request, 'myApp/details-screen.html', context)
    else:
       return HttpResponse("詳細ページが設定されていません")


def Heart_add(request, id):
    userinfo_hearted = get_object_or_404(login, pk=id)
    userdetail_hearted = UserDetail.objects.filter(login_user=userinfo_hearted)
    
    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']

    user = authenticate(username=user_username, password=user_pass)
    login(request, user)

    userinfo = get_object_or_404(login, pk=user.id-1)
    userdetail = UserDetail.objects.filter(login_user=userinfo)

    #データベース追加
    heart_add = Heart.objects.create(login_user=userinfo, heart_user=userinfo_hearted)
    heart_add.save()

   
    if userdetail.exists():
        userinfoMypage = userdetail_hearted[0]
        
        context = {
            'userinfo':userinfo_hearted,
            'userinfoMypage':userinfoMypage,
            'user_username':user_username,
            'user':user,
        }
        return render(request, 'myApp/details-screen.html', context)

    else:
       return HttpResponse("詳細ページが設定されていません")

def Heart_list(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userdetail = Heart.objects.filter(login_user=userinfo)

    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']
    
    user = authenticate(username=user_username, password=user_pass)
    login(request, user)

    context = {
        'userinfo':userinfo,
        'userdetail':userdetail,
        'user':user,
    }

    return render(request, 'myApp/Heart_list.html', context)
    

def create_completion(request):
    return render(request, 'myApp/create_completion.html', {})

#診断
def select(request,id):
    userinfo = get_object_or_404(login, pk=id)
    return render(request, 'myApp/select.html', {'userinfo':userinfo})

#性格診断
def personal_view(request,id):
    userinfo = get_object_or_404(login, pk=id)
    if request.method == 'POST':
        pForm = personalForm(request.POST)
        if pForm.is_valid():
            personalPost = pForm.save(commit=False)
            personalPost.user = userinfo
    params = {
        'title': '性格診断',
        'form':personalForm(),
        'result':None,
        'userinfo':userinfo
    }
    return render(request, 'myApp/personal.html', params)
        
def personal2(request,id):
    userinfo = get_object_or_404(login, pk=id)
    q = question.objects.filter(user=userinfo)
    d = 4 - q[0].q6 + q[0].q1
    c = 4 - q[0].q7 + q[0].q2
    h = 4 - q[0].q8 + q[0].q3
    n = 4 - q[0].q9 + q[0].q4
    o = 4 - q[0].q10 + q[0].q5
    if(personal.objects.filter(user=userinfo).exists()):
        personal.objects.filter(user=userinfo).delete()
    per = personal.objects.create(user=userinfo,diplomacy=d,cooperation=c,honesty=h,nerve=n,openness=o)
    context = {
         'userinfo':userinfo
        }
    
    return render(request, 'myApp/personal2.html', context)

#ユーザ情報を辞書に格納して、users.htmlに返す
def showUsers(request):
    userinfo = login.objects.all()
    context = {
        'msg':'ユーザ数',
        'userinfo':userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myApp/users.html', context)

#URLから受け取ったidを元にユーザの詳細情報を取得、detail.htmlに返す
def showDetail(request,id):
    userinfoDetail = get_object_or_404(login, pk=id)
    context = {
        'userinfoDetail':userinfoDetail,
    }
    return render(request, 'myApp/detail.html', context)


def showCreateUserForm(request):
    #フォームを変数にセット
    params = {
        "AccountCreate":False,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
    }
    params["account_form"] = UserForm()
    params["add_account_form"] = AddUserForm()
    params["AccountCreate"] = False
    return render(request, "myApp/create.html", context=params)

def addUser(request):
    params = {
        "AccountCreate":False,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
    }
    #リクエストがPOSTの場合
    if request.method == 'POST':
        params["account_form"] = UserForm(request.POST)
        params["add_account_form"] = AddUserForm(request.POST,request.FILES)
        
        if params["account_form"].is_valid() and params["add_account_form"].is_valid():
           #アカウント情報をDB保存
                account = params["account_form"].save()
                account.set_password(account.password)
                account.save()

                #追加情報
                add_account = params["add_account_form"].save(commit=False)
                #UserFormとAddUserForm 1vs1 紐付け
                add_account.user = account

                add_account.save()

                #アカウト作成情報更新
                params["AccountCreate"] = True

        else:
                #フォームが有効でない場合
            print(params["account_form"].errors)
            return render(request, 'myApp/create.html', context=params)
        
    return render(request, 'myApp/create_completion.html')


def Login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(username=ID, password=Pass)

        request.session['userpass'] = Pass
        global user_pass
        user_pass = request.session['userpass']

        request.session['user_user_name'] = ID
        global user_username
        user_username = request.session['user_user_name']

        if user:
            if user.is_active:
                #ログイン
                login(request, user)
                userinfo = get_object_or_404(login, pk=user.id-1)
                alluser = login.objects.all()
                user_exclude = login.objects.exclude(id=userinfo.id)
        
                userschool = user_exclude.filter(school_name=userinfo.school_name)
                userschool_random = userschool.order_by('?')[:10]

                usermajor = user_exclude.filter(school_major=userinfo.school_major)
                usermajor_random = usermajor.order_by('?')[:10]
       
                context = {
                    'userinfo':userinfo,
                    'user':user,
                    'alluser':alluser,
                    'userschool_random':userschool_random,
                    'usermajor_random':usermajor_random,
                }

                return render(request, 'myApp/topScreen.html', context)
            else:
                #アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        #ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    #GET
    else:
        return render(request, 'myApp/login_user.html')


#ログアウト
def Logout(request):
    logout(request)
    request.session.clear()
    return render(request, 'myApp/login_user.html')

#ログイン後ホーム
def topScreen(request, id):
    userinfo = get_object_or_404(login, pk=id)


    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']
    
    user = authenticate(username=user_username, password=user_pass)
    login(request, user)
    
    
    alluser = login.objects.all()
    user_exclude = login.objects.exclude(id=userinfo.id)
    
    userschool = user_exclude.filter(school_name=userinfo.school_name)
    userschool_random = userschool.order_by('?')[:10]
    
    usermajor = user_exclude.filter(school_major=userinfo.school_major)
    usermajor_random = usermajor.order_by('?')[:10]
    
    context = {
        'userinfo':userinfo,
        'user':user,
        'alluser':alluser,
        'userschool_random':userschool_random,
        'usermajor_random':usermajor_random,
    }
    
    return render(request, "myApp/topScreen.html",  context)

def UserUpdate(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userUpdateForm = AddUserForm(instance=userinfo)
    context = {
        'userinfo':userinfo,
        'userUpdateForm':userUpdateForm,
    }
    return render(request, 'myApp/user_update.html',context)

def updateUser(request, id):
    if request.method == 'POST':
        userinfo = get_object_or_404(login,pk=id)
        userUpdateForm = AddUserForm(request.POST, request.FILES, instance=userinfo)

        context = {
            'userinfo':userinfo,
            'userUpdateForm':userUpdateForm,
        }
        
        if userUpdateForm.is_valid():
            userUpdateForm.save()
        else:
            print(userUpdateForm.errors)
            return(request, 'myApp/user_update.html', context)
            

    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']
    
    user = authenticate(username=user_username, password=user_pass)
    login(request, user)
    
    
    alluser = login.objects.all()
    user_exclude = login.objects.exclude(id=userinfo.id)
    
    userschool = user_exclude.filter(school_name=userinfo.school_name)
    userschool_random = userschool.order_by('?')[:10]
    
    usermajor = user_exclude.filter(school_major=userinfo.school_major)
    usermajor_random = usermajor.order_by('?')[:10]
    
    params = {
        'userinfo':userinfo,
        'user':user,
        'alluser':alluser,
        'userschool_random':userschool_random,
        'usermajor_random':usermajor_random,
    }

    return render(request, "myApp/topScreen.html",  context=params)

def showUserDetail(request, id):
    userinfo = get_object_or_404(login, pk=id)
    #フォームを変数にセット
    params = {
        "userinfo":userinfo,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
        "user_detail_form":UserDetailForm(),
    }
    params["account_form"] = UserForm()
    params["add_account_form"] = AddUserForm()
    params["user_detail_form"] = UserDetailForm()
    return render(request, "myApp/user_adddetail.html", context=params)

def addUserDetail(request ,id):
    userinfo = get_object_or_404(login, pk=id)
    params = {
        "userinfo":userinfo,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
        "user_detail_form":UserDetailForm(),
    }
    if request.method == 'POST':
        userDetailForm = UserDetailForm(request.POST, request.FILES)
        if  userDetailForm.is_valid():
            userDetailPost = userDetailForm.save(commit=False)
            userDetailPost.login_user = userinfo
            userDetailPost.save()

        else:
            #フォームが有効でない場合
            print(userDetailForm.errors)
            return render(request, 'myApp/user_adddetail.html', context=params)


    userdetail = UserDetail.objects.filter(login_user=userinfo)
    userinfoMypage = userdetail[0]
    mypagetext = {
            'userinfo':userinfo,
            'userinfoMypage':userinfoMypage
    }
    return render(request, 'myApp/mypage.html', context=mypagetext)


def showMypage(request,id):
    userinfo = get_object_or_404(login, pk=id)
    userdetail = UserDetail.objects.filter(login_user=userinfo)

    global user_pass
    user_pass = request.session['userpass']

    global user_username
    user_username = request.session['user_user_name']
    
    user = authenticate(username=user_username, password=user_pass)
    login(request, user)   

    if userdetail.exists():
        userinfoMypage = userdetail[0]
        
        context = {
            'userinfo':userinfo,
            'userinfoMypage':userinfoMypage,
            'user':user,
        }
        return render(request, 'myApp/mypage.html', context)

    else:
        params = {
        "userinfo":userinfo,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
        "user_detail_form":UserDetailForm(),
        }
        params["account_form"] = UserForm()
        params["add_account_form"] = AddUserForm()
        params["user_detail_form"] = UserDetailForm()
        return render(request, "myApp/user_adddetail.html", context=params)

def MypageUpdate(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userdetail = UserDetail.objects.filter(login_user=userinfo)

    if userdetail.exists():
        #userinfoMypage = get_object_or_404(UserDetail, pk=id)
        userinfoMypage = userdetail[0]
        user_detail_form = UserDetailForm(instance=userinfoMypage)
        context = {
            'userinfoMypage':userinfoMypage,
            'user_detail_form':user_detail_form,
        }
        return render(request, 'myApp/mypage_update.html',context)
    else:
        return HttpResponse("詳細ページが設定されていません")


def updateMypage(request,id):
    
    if request.method == 'POST':
        userinfoMypage = get_object_or_404(UserDetail,pk=id)
        user_detail_form = UserDetailForm(request.POST, request.FILES, instance=userinfoMypage)
        if user_detail_form.is_valid():
            user_detail_form.save()


    userinfo = get_object_or_404(login, pk=id)      
    context = {
        'userinfo':userinfo,
        'userinfoMypage':userinfoMypage
    }
    
    return render(request, 'myApp/mypage.html', context)


def UserCheckDelete(request, id):
    userinfo = get_object_or_404(login,pk=id)
    context = {
        'userinfo':userinfo
    }
    return render(request, 'myApp/user_delete.html', context)
    
def UserDelete(request, id):
    userinfo = get_object_or_404(login,pk=id)
    userinfo.delete()
    userinfo.user.delete()
    return render(request, 'myApp/new_register.html')
    

#趣味診断
def showSelectHobby(request,id):
    userinfo = get_object_or_404(login, pk=id)

    params = {
        "userinfo":userinfo,
        "favorite_hobby":SelectHobby(),
    }
    params["favorite_hobby"] = SelectHobby()
    return render(request, 'myApp/selectHobby.html', context=params)


def addSelectHobby(request,id):
    userinfo = get_object_or_404(login, pk=id)
    params = {
        "userinfo":userinfo,
        "favorite_hobby":SelectHobby(),
    }
    if request.method == "POST":
        selectHobbyForm = SelectHobby(request.POST, request.FILES)      
        if selectHobbyForm.is_valid():
            selectHobbyPost = selectHobbyForm.save(commit=False)
            selectHobbyPost.login_user = userinfo
            selectHobbyPost.save()
            
        else:
            print(params["favorite_hobby"].errors)
            return render(request, 'myApp/selectHobby.html', context=params)

    userhobby = hobby.objects.filter(login_user=userinfo)
    userselectHobby = userhobby[0]

    mypagetext = {
        'userinfo':userinfo,
        'userselectHobby':userselectHobby,
    }
        
    return render(request, 'myApp/new_register.html', context=mypagetext)


def showUpdateSelectHobby(request,id):
    userinfoHobby = get_object_or_404(hobby, pk=id)
    favorite_hobby = SelectHobby(instance=userinfoHobby)
  
    context = {
        'userinfoHobby':userinfoHobby,
        'favorite_hobby':favorite_hobby,
    }
    return render(request, 'myApp/update_selectHobby.html', context)
   

def updateSelectHobby(request, id):
    if request.method == "POST":
        userinfoHobby = get_object_or_404(hobby, pk=id)
        favorite_hobby = SelectHobby(request.POST, request.FILES, instance=userinfoHobby)
        if favorite_hobby.is_valid():
            favorite_hobby.save()

    userinfoHobby = get_object_or_404(hobby, pk=id)
    context = {
        'userinfoHobby':userinfoHobby,
    }
    
    return render(request, 'myApp/new_register.html', context)

