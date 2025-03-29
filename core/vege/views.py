from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q , Sum
# Create your views here.

@login_required(login_url="/login/")
def recepies(request):
    if request.method == "POST":

        data = request.POST 
        r_image = request.FILES.get('r_image')
        r_name = data.get("r_name")
        r_description = data.get("r_description")
        
        Receipe.objects.create(
            r_image = r_image,
            r_name = r_name,
            r_description = r_description,
        )
        return redirect('/')
    
    queryset = Receipe.objects.all()


    if request.GET.get('search_re'):
        queryset = queryset.filter(r_name__icontains = request.GET.get('search_re'))

    context = {'receipes':queryset}
    return render(request, 'recipies.html' , context)


def update_rec(request , id):
    queryset  = Receipe.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        r_image = request.FILES.get('r_image')
        r_name = data.get("r_name")
        r_description = data.get("r_description")

        queryset.r_name = r_name
        queryset.r_description = r_description

        if r_image:
            queryset.r_image = r_image
        
        queryset.save()
        return redirect('/')
    context = {'receipe':queryset}
    return render(request, 'update_rec.html' , context)

def delete_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request , 'Invalid Username')
            return redirect('/login')
    
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request , 'Invalid Password')
            return redirect('/login')
        else:
            login(request , user)
            return redirect('/')
    
    
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register_page(request):
    if request.method == "POST":
        first_name  =  request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'Username already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name ,
            last_name = last_name ,
            username = username,
            )
        
        user.set_password(password)
        user.save()

        messages.success(request , 'User created successfully')
        return redirect('/register/')
    return render(request , 'register.html')

def get_students(request):

     
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(S_name__icontains = search)

    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    # print(page_obj)
    return render (request , 'reports/students.html' , {'queryset' : page_obj})

def see_marks(request , S_Id):
    queryset = SubjectMarks.objects.filter(student__S_Id__S_Id = S_Id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    return render(request , 'reports/see_marks.html' , {'queryset' : queryset , 'total_marks' : total_marks , 'Id':S_Id})