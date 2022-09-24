from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','password1','password2')


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        #self.fields['username']

        self.fields['username'].widget.attrs.update({'class':'form-control bg-transparent','placeholder':'Username', 'autocomplete':'off'})
        self.fields['password1'].widget.attrs.update({'class':'form-control bg-transparent','placeholder':'Password', 'autocomplete':'off'})
        self.fields['password2'].widget.attrs.update({'class':'form-control bg-transparent','placeholder':'Repeat Password', 'autocomplete':'off'})


        #self.fields['username'].widget = TextInput(attrs={'id':'form-control'})

        




        #self.fields['username'].widget = TextInput(attrs={'id': 'myCustomId','class': 'myCustomClass','name': 'myCustomName','placeholder': 'myCustomPlaceholder'})        
        
        #self.fields['username'].widget.attrs.update({'class': 'form-control bg-transparent'})

        #self.fields['username'].widget.attrs['class'] = 'form-control bg-transparent'
        #self.fields['password1'].widget.attrs['class'] = 'form-control'
        #self.fields['password2'].widget.attrs['class'] = 'form-control'
