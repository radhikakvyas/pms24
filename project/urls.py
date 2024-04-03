from django.contrib import admin
from django.urls import path,include
from .views import ProjectCreationView,ProjectListView,ProjectDeleteView,ProjectDetailView,ProjectUpdateView,ProjectTeamCreationView,ProjectTeamDetailView,ProjectTeamUpdateView,ProjectModuleCreationView,ProjectModuleListView,ProjectModuleListViews,ProjectModuleDetailView,ProjecModuleDeleteView,ProjectModuleUpdateView,ProjectStatusCreationView,ProjectTaskCreationView,ProjectTaskDetailView,ProjectTaskUpdateView,ProjectTaskListView,UserTaskCreationView,UserTaskListView,ProjectTaskListViews
from .import views


urlpatterns = [
    #-------------------------Project Model------------------------
    path("create/",ProjectCreationView.as_view(),name="CreateProject"),
    path("list/",ProjectListView.as_view(),name="ListProject"),
    path("detail/<int:pk>/",ProjectDetailView.as_view(),name="DetailProject"),
    path("delete/<int:pk>/",ProjectDeleteView.as_view(),name="DeleteProject"),
    path("update/<int:pk>/",ProjectUpdateView.as_view(),name="UpdateProject"),
    
    #-------------------------Project Team Model------------------------
    path("create_team/",ProjectTeamCreationView.as_view(),name="CreateTeamProject"),    
    path("detail_team/<int:pk>/",ProjectTeamDetailView.as_view(),name="DetailTeamProject"),
    path("update_team/<int:pk>/",ProjectTeamUpdateView.as_view(),name="UpdateTeamProject"),
    
    #-------------------------Project Status Model------------------------
    path("create_status/",ProjectStatusCreationView.as_view(),name="CreateStatusProject"),

    #-------------------------Project Module Model------------------------
    path("create_module/",ProjectModuleCreationView.as_view(),name="CreateModuleProject"),
    path("list_module/",ProjectModuleListView.as_view(),name="ListModuleProject"),
    path("list_modules/",ProjectModuleListViews.as_view(),name="ListModuleProjects"),
    path("deatil_module/<int:pk>/",ProjectModuleDetailView.as_view(),name="DetailModuleProject"),
    path("delete_module/<int:pk>/",ProjecModuleDeleteView.as_view(),name="DeleteModuleProject"),
    path("upadate_module/<int:pk>/",ProjectModuleUpdateView.as_view(),name="UpdateModuleProjectView"),

    #-------------------------Project Task Model----------------------------
    path("create_task/",ProjectTaskCreationView.as_view(),name="CreateTaskProject"),
    path("list_task/",ProjectTaskListView.as_view(),name="ListTaskProject"),
    path("list_tasks/",ProjectTaskListViews.as_view(),name="ListTaskProjects"),
    path("detail_task/<int:pk>/",ProjectTaskDetailView.as_view(),name="DetailTaskProject"),
    path("update_task/<int:pk>/",ProjectTaskUpdateView.as_view(),name="UpdateTaskProject"),

    #-----------------------Chart--------------------------------------------
    path("chart/",views.Chart,name="Chart"),

    #-----------------------------------User Task Model------------------------
    path("usertask_create/",UserTaskCreationView.as_view(),name="UserTask"),
    path("usertask_list/",UserTaskListView.as_view(),name="UserTaskList"),
    
    

]
