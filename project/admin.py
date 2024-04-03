from django.contrib import admin
from .models import Project,ProjectTeam,ProjectModule,Status,UserTask,Task

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTeam)
admin.site.register(ProjectModule)
admin.site.register(Status)
admin.site.register(UserTask)
admin.site.register(Task)