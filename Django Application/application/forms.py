from django import forms

from application.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your name'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your course'})
        }