from django import forms

class UsersForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=30, required=True)
    user_surname = forms.CharField(label='Surname', max_length=30, required=True)
    user_dateOfBirth = forms.DateField(label='Date of birth', widget=forms.TextInput(attrs={'placeholder': ' yyyy-mm-dd'}) , required=True)
    user_login = forms.CharField(label='Login', max_length=30, required=True)