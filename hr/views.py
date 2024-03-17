from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from employee.models import Employee  
from django.contrib import messages
from hr.models import Hr
from django.http import HttpResponse

# Create your views here.
def login(request):
    # cookie = request.COOKIES.get('login') 
    # print('cookie',cookie)
    # to check if user login or not
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       print(username,password)
       user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)
           
            return redirect('admin_login')
            
    else:
            # Return an invalid login error message
        messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')

"""def dash(request):
     employee=Employee.objects.all()
     return render(request,'dash.html',{'employee':employee})

def delete(request, id):
     employee=Employee.objects.get(id=id)
     employee.delete()
     return redirect("/dash")"""