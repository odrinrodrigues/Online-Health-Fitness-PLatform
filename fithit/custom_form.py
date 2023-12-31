from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your tests here.

###Form Validators
def pass_lenth(value):
    if len(value)<8:
        raise forms.ValidationError("the Password is too short")
    return value

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':_('Name')})
        self.fields['username'].widget.attrs.update({'placeholder':_('Username')})
        self.fields['email'].widget.attrs.update({'placeholder':_('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':_('Repeat password')})
   
class loginform(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'placeholder':_('Username')})
        
        self.fields['password'].widget.attrs.update({'placeholder':_('Password')})        


    # username=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _("Email")}),max_length=50,required=True,validators=[pass_lenth,])
    # password=forms.CharField(max_length=30,required=True,widget=forms.PasswordInput(attrs={ 'placeholder': 'Password'}),validators = [pass_lenth, ])