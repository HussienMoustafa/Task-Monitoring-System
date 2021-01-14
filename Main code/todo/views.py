from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import Group, User, auth
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from datetime import datetime
from datetime import timedelta
from django.db.models import Sum
from django.db.models import Count
from .models import *
from .forms import *
from .decorators import *
from _datetime import timezone
# Create your views here.
@unauthenticated_user
def TaskListView(request):
    user_created = datetime.now(timezone.utc)-request.user.date_joined
    sum_rate_last30 = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=30)).aggregate(Sum('rate')).get('rate__sum', 0.00)
    sum_rate_last30_count = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=30)).count()    
    profile = UserProfile.objects.get(user=request.user)
    membership_day = profile.membership_day
    membership_db = profile.membership
    dt = datetime.now()
    dt = dt.strftime("%m")    
    try:
        final_rate_last30 = sum_rate_last30 / (sum_rate_last30_count*10) * 100
    except:
        final_rate_last30 = 0
    try:
        get_todo = Todo.objects.filter(user=request.user).order_by('id')
    except:
        get_todo = ''
    if user_created < timedelta(days=30) and final_rate_last30 == 0:
        membership = "Normal"
    elif user_created < timedelta(days=30) and final_rate_last30 > 0:
        membership = "Bronze"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and final_rate_last30 < 80 and membership_day != dt:
        membership = "Bronze"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and 80 <= final_rate_last30 < 90 and membership_day != dt:
        membership = "Silver"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and final_rate_last30 >=90 and membership_day != dt:
        membership = "Golden"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()        
    else:
        membership = membership_db
    context = {'get_todo':get_todo,'membership':membership}
    return render(request,'todo_list.html',context)

def AddTaskView(request):
    if request.method=="POST":
        form = TodoForm(request.POST)
        user = request.user
        task = request.POST['task']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.user = user
            formsave.save()
        else:
            print("EEROORR")
    else:
        form = TodoForm()
    context = {'form':form}
    return save_all(request,form,'add_task.html')

def EditTaskView(request,id):
	todo = get_object_or_404(Todo,id=id)
	if request.method == 'POST':
		form = TodoEditForm(request.POST,instance=todo)
	else:
		form = TodoEditForm(instance=todo)
	return save_all(request,form,'edit_task.html') 

def DeleteTaskView(request,id):
	data = dict()
	todo = get_object_or_404(Todo,id=id)
	if request.method == "POST":
		todo.delete()
		data['form_is_valid'] = True
		todo = Todo.objects.all()
		data['todo_list'] = render_to_string('todo_list2.html',{'todo':todo})
	else:
		context = {'todo':todo}
		data['html_form'] = render_to_string('delete_task.html',context,request=request)
	return JsonResponse(data)

def save_all(request,form,template_name):
    data = dict()
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.user = user
            try:
                if request.POST['is_finished'] == 'No':
                    formsave.rate = 0
            except:
                pass
            formsave.save()
            data['form_is_valid'] = True
            get_todo = Todo.objects.all().order_by('-id')
            data['todo_list'] = render_to_string('todo_list2.html',{'get_todo':get_todo})
        else:
            data['form_is_valid'] = False
    context = {'form':form} 
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Try again')
    context = {}
    return render(request, 'login.html',context)

def RegisterView(request): 
    if request.method=="POST":
        email = request.POST['email']
        first_name = request.POST['first_name'].capitalize()
        last_name = request.POST['last_name'].capitalize()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        mail_exist = User.objects.filter(email=email).exists()
        username_exist = User.objects.filter(username=email).exists()
        if mail_exist or username_exist:
            messages.info(request,'Existing E-Mail')
        elif password1 != password2:
            messages.info(request,"Password doesn't match !")
        else:
            user = User.objects.create_user(username=email,email=email,password=password1,first_name=first_name,last_name=last_name)
            return redirect('/login/')
    else:
        pass
    context = {}
    return render(request,'register.html',context)

def LogoutView(request):
    auth.logout(request)
    return redirect('/login/')

@unauthenticated_user
def RepView(request):
    try:
        all_tasks = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).count()
        sum_rate = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).aggregate(Sum('rate')).get('rate__sum', 0.00)
        sum_rate_count = Todo.objects.filter(user=request.user,is_finished="Yes",created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).count()
        get_all_tasks = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).order_by('id')
        finished_tasks = Todo.objects.filter(user=request.user,is_finished="Yes",created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).count()
        progress_tasks = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=7)).exclude(is_finished="Yes").count()
        final_rate = sum_rate / (sum_rate_count*10) * 100
    except:
        #all_tasks = ""
        sum_rate_count = ""
        sum_rate = ""
        #get_all_tasks = ""
        finished_tasks = "0"
        progress_tasks = "0"
        final_rate = "0"
    context = {'all_tasks':all_tasks,'finished_tasks':finished_tasks,'progress_tasks':progress_tasks,'get_all_tasks':get_all_tasks,'final_rate':final_rate}
    return render(request,'rep.html',context)

@unauthenticated_user
def ProfileView(request):
    profile = UserProfile.objects.get(user=request.user)
    all_tasks = Todo.objects.filter(user=request.user).count()
    sum_rate = Todo.objects.filter(user=request.user).aggregate(Sum('rate')).get('rate__sum', 0.00)
    sum_rate_count = Todo.objects.filter(user=request.user,is_finished="Yes").count()
    membership_day = profile.membership_day
    membership_db = profile.membership
    dt = datetime.now()
    dt = dt.strftime("%m")
    try:
        final_rate = sum_rate / (sum_rate_count*10) * 100
    except:
        final_rate = 0
    user_created = datetime.now(timezone.utc)-request.user.date_joined
    sum_rate_last30 = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=30)).aggregate(Sum('rate')).get('rate__sum', 0.00)
    sum_rate_last30_count = Todo.objects.filter(user=request.user,created_at__lte= datetime.now(),created_at__gte= datetime.now()-timedelta(days=30)).count()
    try:
        final_rate_last30 = sum_rate_last30 / (sum_rate_last30_count*10) * 100
    except:
        final_rate_last30 = 0
    if user_created < timedelta(days=30) and final_rate_last30 == 0:
        membership = "Normal"
    elif user_created < timedelta(days=30) and final_rate_last30 > 0:
        membership = "Bronze"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and final_rate_last30 < 80 and membership_day != dt:
        membership = "Bronze"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and 80 <= final_rate_last30 < 90 and membership_day != dt:
        membership = "Silver"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()
    elif user_created > timedelta(days=30) and final_rate_last30 >=90 and membership_day != dt:
        membership = "Golden"
        profile.membership_day = dt
        profile.membership = membership
        profile.save()        
    else:
        membership = membership_db
    context = {'all_tasks':all_tasks,'final_rate':final_rate,'profile':profile,'membership':membership}
    return render(request,'profile.html',context)

def HallOfFame(request):
    try:
        x = sorted(UserProfile.objects.all(),  key=lambda m: 'm.t_rate')
    except:
        x = 1
    context = {'x':x}
    return render(request,'top_users.html',context)

