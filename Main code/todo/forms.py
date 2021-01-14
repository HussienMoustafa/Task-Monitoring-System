from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todo


class TodoForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(format = '%d/%m/%Y %H:%M:%S',attrs={'required ': True, 'placeholder': 'Start Date','autocomplete':'off'}),input_formats=('%d/%m/%Y %H:%M:%S',))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(format = '%d/%m/%Y %H:%M:%S',attrs={'required ': True, 'placeholder': 'End Date','autocomplete':'off'}),input_formats=('%d/%m/%Y %H:%M:%S',))
    class Meta:
        model = Todo
        fields = ['user','task','start_date','end_date']
        labels = {}
    
        widgets = {
            'task': forms.TextInput(attrs={'required ': True, 'placeholder': 'Task','autocomplete':'off'}),
            #'is_finished': forms.TextInput(attrs={'required ': False}),
            #'rate': forms.NumberInput(attrs={'required ': False}),
        }

class TodoEditForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(format = '%d/%m/%Y %H:%M:%S',attrs={'required ': True, 'placeholder': 'Start Date','autocomplete':'off'}),input_formats=('%d/%m/%Y %H:%M:%S',))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(format = '%d/%m/%Y %H:%M:%S',attrs={'required ': True, 'placeholder': 'End Date','autocomplete':'off'}),input_formats=('%d/%m/%Y %H:%M:%S',))
    class Meta:
        model = Todo
        fields = ['user','task','start_date','end_date','is_finished','rate']
        labels = {}
    
        widgets = {
            'task': forms.TextInput(attrs={'required ': True, 'placeholder': 'Task','autocomplete':'off'}),
            'is_finished': forms.Select(attrs={'required ': False}),
            'rate': forms.Select(attrs={'required ': False}),
        }

