from django import forms
from django.forms import ModelForm
from temp3.models import temp3model

class temp3Form(ModelForm):
    class Meta:
        model = temp3model
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Enter Image'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Degree'}),
            'propoint_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1)'}),
            'propoint_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2)'}),
            'propoint_3': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': '3)'}),
            'propoint_4': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': '4)'}),
            'lang_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Language 1'}),
            'lang_2': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Enter Language 2'}),
            'lang_3': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Enter Language 3'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'Date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd-mm-yyyy'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Name'}),
            'mobileno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'course_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Course 10th '}),
            'school_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School 10th'}),
            'percent_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percent 10th'}),
            'year_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year 10th'}),
            'course_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course 12th'}),
            'school_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School 12th'}),
            'percent_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percent 12th'}),
            'year_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year 12th'}),
            'course_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Graduation'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College'}),
            'percent_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percent Graduation'}),
            'year_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year Graduation'}),
            'skill_1': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Skill 1'}),
            'skill_2': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Skill 2'}),
            'skill_3': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Skill 3'}),
            'skill_4': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Skill 4'}),
            'skill_5': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Skill 5'}),
            'hobby_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hobby 1'}),
            'hobby_2': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Hobby 2'}),
            'hobby_3': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Hobby 3'}),
            'intern_1': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Intern 1'}),
            'intern_2': forms.TextInput(attrs={'required': False,'class': 'form-control', 'placeholder': 'Intern 2'}),
            'declare': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Declaration'}),

        }

    

