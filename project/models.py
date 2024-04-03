from django.db import models
from user.models import User

# Create your models here.
techChoices = (
    ("Python","Python"),
    ("Java","Java"),
    ("C","C"),
    ("C++","C++"),
    ("C#","C#"),
    (".Net",".Net"),
)

statChoices = (
    ("Completed","Completed"),
    ("In-progress","In-progress"),
    ("Not-started","Not-started"),
)

prioChoices = (
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimatedHours = models.PositiveIntegerField()
    startDate = models.DateField()
    completionDate = models.DateField()

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name
       
class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "projectteam"

    def __str__(self):
        return self.user.username

class Status(models.Model):
    statusName = models.CharField(max_length=100)

    class Meta:
        db_table = "status"
    
    def __str__(self):
        return self.statusName

class ProjectModule(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    moduleName = models.CharField(max_length=100)
    description = models.TextField()
    estimatedHours = models.DurationField()
    status = models.CharField(max_length=100,choices=statChoices)
    startDate = models.DateField()

    class Meta:
        db_table = "projectmodule"

    def __str__(self):
        return self.moduleName
    
class Task(models.Model):
    module = models.ForeignKey(ProjectModule,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    status = models.CharField(choices=statChoices,null=True,max_length=100)
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=prioChoices)    
    description = models.TextField()
    totalMinutes = models.PositiveIntegerField()
    
    class Meta:
        db_table = "task"

    def __str__(self):
        return self.title
    
    

class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = "usertask"

    def __str__(self):
        #return self.user.username
        return self.task.title +" - "+ self.user.username

    