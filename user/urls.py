from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth.views import LogoutView
from .views import UpdateStatusView


urlpatterns = [
    path("sendmail/",views.sendMail,name="sendMail"),
    path("manager_register/",views.ManagerRegisterView.as_view(),name="manager_register"),
    path("developer_register/",views.DeveloperRegisterView.as_view(),name="developer_register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("logout/",views.LogoutView,name="logout"),
    path("manager_dashboard/",views.ManagerDashboardView.as_view(),name="manager_dashboard"),
    path("developer_dashboard/",views.DeveloperDashboardView.as_view(),name="developer_dashboard"),
    
    #----------------------------------Update status view-----------------------
    path("updatestatustask/<int:pk>/",views.UpdateStatusView.as_view(),name="update_status"),

    #----------------------------------Report-----------------------------------
    
    path("reports/<int:pk>/",views.ProjectReport,name="Report"),

    #----------------------------------Password------------------
    
]
