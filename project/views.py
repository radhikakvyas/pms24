from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ProjectCreationForm,ProjectTeamCreationForm,ProjectModuleCreationForm,ProjectStatusCreationForm,ProjectTaskCreationForm,UserTaskCreationForm
from .models import Project,ProjectTeam,ProjectModule,Status,Task,UserTask

# Create your views here.
#----------------------------Project Model----------------------------
class ProjectCreationView(CreateView):
    template_name = 'project/create_project.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'

class ProjectListView(ListView):
    template_name = 'project/list_project.html'
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "projects"
    template_name = 'project/detail_project.html'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete_project.html'
    success_url = '/project/list/'

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/update_project.html'
    success_url = '/project/list/'

#----------------------------Project Team Model----------------------

class ProjectTeamCreationView(CreateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    template_name = 'project/create_project_team.html'
    success_url = '/project/list/'

class ProjectTeamDetailView(DetailView):
    model = ProjectTeam
    context_object_name = 'projects'
    template_name = 'project/detail_project_team.html'

class ProjectTeamUpdateView(UpdateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    template_name = 'project/update_project_team.html'
    success_url = '/project/list/'

#------------------------------Project Status Model-------------------
class ProjectStatusCreationView(CreateView):
    model = Status
    form_class = ProjectStatusCreationForm
    template_name = 'project/create_project_status.html'
    success_url = '/project/list_module/'

#-------------------------------Project Module Model------------------
class ProjectModuleCreationView(CreateView):
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    template_name = 'project/create_project_module.html'
    success_url = '/project/list_module/'

class ProjectModuleListView(ListView):
    template_name = 'project/list_project_module.html'
    model =  ProjectModule
    context_object_name = 'modules'

class ProjectModuleListViews(ListView):
    template_name = 'project/list_project_modules.html'
    model =  ProjectModule
    context_object_name = 'modules'

class ProjectModuleDetailView(DetailView):
    model = ProjectModule
    context_object_name = 'modules'
    template_name = 'project/detail_project_module.html'

class ProjecModuleDeleteView(DeleteView):
    model = ProjectModule
    template_name = 'project/delete_project_module.html'
    success_url = '/project/list_module/'

class ProjectModuleUpdateView(UpdateView):
    model = ProjectModule
    form_class = ProjectModuleCreationForm
    template_name = 'project/update_project_module.html'
    success_url = '/project/list_module/'

#----------------------Project Task Model-------------------------
    
class ProjectTaskCreationView(CreateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = 'project/create_project_task.html'
    success_url = '/project/list_task/'

class ProjectTaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'project/list_project_task.html'

class ProjectTaskListViews(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'project/list_project_tasks.html'

class ProjectTaskDetailView(DetailView):
    model = Task
    context_object_name = "tasks"
    template_name = 'project/detail_project_task.html'

class ProjectTaskUpdateView(UpdateView):
    model = Task
    form_class = ProjectTaskCreationForm
    template_name = 'project/update_project_task.html'
    success_url = '/project/list_task/'


#--------------------------Chart------------------------------------

def Chart(request):
    labels = []
    data = []
    
    queryset = Project.objects.order_by('-estimatedHours')[:7]
    
    for project in queryset:
        labels.append(project.name)
        data.append(project.estimatedHours)
        
    return render(request, 'project/chart.html',{
        'labels':labels,
        'data':data
    })        

#-------------------------------UserTask Model----------------


class UserTaskCreationView(CreateView):
    model = UserTask
    form_class = UserTaskCreationForm
    template_name = 'project/user_task_create.html'
    success_url = '/project/list/'

class UserTaskListView(ListView):
    model = UserTask
    context_object_name = 'usertasks'
    template_name = 'project/user_task_list.html'