from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import User
from .forms import ManagerRegistrationForm,DeveloperRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import ListView
from django.conf import settings
from django.core.mail import send_mail
from project.models import Project,UserTask,Task,ProjectModule,Status
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class ManagerRegisterView(CreateView):
    template_name = 'user/manager_register.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/user/login/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("Email...",email)
        if sendMail(email):
            print("Mail sent successfully..")
            return super().form_valid(form)
        else:
            return super().form_valid(form)

class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'

#def sendMail(request):
def sendMail(to):
    subject = 'Welcome to pms'
    message = 'Hope you are enjoying your django tutorial'
    #recepientList = ["radhikavyas132@gmail.com"]
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER 
    
    send_mail(subject,message,EMAIL_FROM,recepientList)
    return True
    #return HttpResponse("Email sent")

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    model = User

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager_dashboard/'
            else:
                return '/user/developer_dashboard/'

def LogoutView(request):
    logout(request)
    return redirect("/user/login/")

@method_decorator(login_required, name='dispatch')
class ManagerDashboardView(ListView):
    
    def get(self, request, *args,**kwargs):
        #here logic to all the projects 
        print("ManagerDashboardView")
        #--------------------------For status wise task------------------
        tasks = UserTask.objects.all() #display task 
        print("......",tasks)
        
        #----------------Display Dashboard----------------
        projects = Project.objects.all() #select * from project  count project total
        
        priority = Task.objects.filter(priority='High') # count high priority task
        
        notstarted = Task.objects.filter(status='Not-started') # count not started task
        
        pending = Task.objects.filter(status__in=['In-progress', 'Not-started']) # pending tassk includ in progress and not started
                
        context ={
            'projects':projects,
            'tasks':tasks,
            'priority':priority,
            'pending':pending,
            'notstarted':notstarted
        }
        return render(request, 'user/manager_dashboard.html',context)
    
    template_name = 'user/manager_dashboard.html'

@method_decorator(login_required, name='dispatch')
class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #here logic to all the projects 
        #----------------------------Update status wise task-----------------
        
        tasks = UserTask.objects.all() # for task display for update  status and total task count
        usertasks = UserTask.objects.filter(user=request.user).values()
        print("......",usertasks)        
        
        #---------------------------------Dashboard display---------
        projects = Project.objects.all() # for total project count
                
        modules = ProjectModule.objects.all() # for total module count
        
        pending = Task.objects.filter(status__in=['In-progress', 'Not-started']) # pending tassk includ in progress and not started
        context ={
            'projects':projects,
            'tasks': tasks,        
            'modules':modules,
            'pending':pending,
            'usertasks':usertasks        
        }
        return render(request, 'user/developer_dashboard.html',context)    
    template_name = 'user/developer_dashboard.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("Email...",email)
        if sendMail(email):
            print("Mail sent successfully..")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
  
#------------------------------Task Status Update--------------

class UpdateStatusView(View):    
    def post(self,request,pk):
        print("Pk...",pk)          
        task = Task.objects.get(id=pk)
        print("Task....",task)          
        print("Task Updated..") 
        #task.status.statusName = "In-progress"   In-progress  Not-started Completed
        if task.status == "Not-started":
            print("not started")            
            task.status = "In-progress"            
        elif task.status == "In-progress":
            task.status = "Completed"
        
        task.save()
        return redirect(reverse('developer_dashboard')) #lazy reverse

#-----------------------------------Report---------------------------
def ProjectReport(request,pk):
    
    usertasks = UserTask.objects.get(pk=pk)
    projects = Project.objects.get(pk=pk)
    project_data = []
    
    modules = ProjectModule.objects.filter(project=projects)
    project_time = projects.estimatedHours
        
    module_data = []
    for module in modules:
            tasks  = Task.objects.filter(module=module)
            module_time = tasks.aggregate(Sum('totalMinutes'))['totalMinutes__sum'] or 0
            module_data.append({
                'module_name': module.moduleName,
                'module_status': module.status,                
                'module_time': module.estimatedHours,
                'tasks': tasks                
            })	
            project_time += module_time
        
    project_data.append({
            'project_name': projects.name,
            'project_time': project_time,
            'modules' :module_data
        })
    return render(request,'user/report.html',{'projects': project_data,'usertasks':usertasks})


#------------------------Forgot Password------------------------
