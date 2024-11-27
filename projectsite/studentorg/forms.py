from django.forms import ModelForm
from django import forms
from .models import Organization
from .models import OrgMember
from .models import College 
from .models import Program
from .models import Student

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'})
        }

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

