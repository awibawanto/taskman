from django import forms
from .models import Staff, TaskStatus


class TaskForm(forms.Form):
    name = forms.CharField(max_length=256)
    description = forms.CharField(max_length=1024)
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    due_date = forms.DateField(widget=forms.SelectDateWidget())
    deliverable = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    staff_pic = forms.ChoiceField(choices=[(staff.user.id, staff.user.username) for staff in Staff.objects.all()])
    status = forms.ChoiceField(choices=[(tag, tag.value) for tag in TaskStatus])


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=256)
    members = forms.MultipleChoiceField(choices=[(staff.user.id, staff.user.username) for staff in Staff.objects.all()], widget=forms.SelectMultiple(), required=False)


class LoginForm(forms.Form):
    login = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ('user',)
