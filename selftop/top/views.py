from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import View
from django.db import IntegrityError
from top.models import HomeworkModel
from django.core.files.storage import FileSystemStorage
class Topself(View):
    def index(request:HttpRequest)->TemplateResponse:
        if request.user.pk == None:
            return render(request, 'selftop/index.html')

        else:
            return render(request, 'selftop/index.html')

    def sign_up(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            return render(request, 'selftop/sign_up.html', context={'form':UserCreationForm})
        if request.method == 'POST':
            try:
                if request.POST['password1']== request.POST['password2']:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('top-index')
                else:
                    return render(request, 'selftop/sign_up.html', context={'form':UserCreationForm,'error':'Password is not match'})
            except IntegrityError:
                return render(request, 'selftop/sign_up.html', context={'form':UserCreationForm,'error':'User is already exsist'})

    def log_in(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            return render(request, 'selftop/log_in.html', context={'form':AuthenticationForm})
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is None:
                return render(request, 'selftop/log_in.html', context={'from':AuthenticationForm, 'error':'Username or password doesnt exists'})
            else:
                login(request,user)
                return redirect('top-index')

    def log_out(request:HttpRequest)->TemplateResponse:
        if request.method == 'POST':
            logout(request)
            return render(request, 'selftop/index.html')

    def toppage(request:HttpRequest)->TemplateResponse:
        if request.method == 'GET':
            homeworks = HomeworkModel.objects.filter(user=request.user)
            return render(request, 'selftop/toppage.html', context={'homeworks': homeworks})
        if request.method == 'POST':
            homeworks = HomeworkModel.objects.filter(user=request.user)
            file = request.FILES['myfile1']
            fs = FileSystemStorage()

            filename = fs.save(file.name, file)

            file_url = fs.url(filename)
            return render(request, 'selftop/toppage.html', {'file_url': file_url,'homeworks': homeworks})

    def homework(request:HttpRequest, home_id:int):
        if request.method == 'GET':
            homework = get_object_or_404(HomeworkModel,pk=home_id)
            return render(request, 'selftop/homework.html', context={'homework':homework})

        if request.method == 'POST':
            homework = get_object_or_404(HomeworkModel,pk=home_id)
            file1 = request.FILES['myfile1']
            fs = FileSystemStorage()
            homework.file = file1
            homework.save()
            filename = fs.save(file1.name, file1)

            file_url = fs.url(filename)
            return render(request, 'selftop/homework.html', {'file_url': file_url, 'homework': homework})







