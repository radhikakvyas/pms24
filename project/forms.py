from django import forms
from .models import Project,ProjectTeam,ProjectModule,Status,Task,UserTask

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        
        widgets = {
            'startDate': forms.DateInput(attrs={'type':'date'}),    
            'completionDate': forms.DateInput(attrs={'type':'date'})
        }

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields = '__all__'

class ProjectModuleCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'

        widgets = {
            'startDate': forms.DateInput(attrs={'type':'date'}),    
            'completionDate': forms.DateInput(attrs={'type':'date'})
        }

class ProjectStatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class ProjectTaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class UserTaskCreationForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = '__all__'