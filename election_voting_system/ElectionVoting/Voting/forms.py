from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate , password_validation
from django import forms
from django.core.exceptions import ValidationError
from django.db.models.fields import CharField
import re
from .models import Voter


class VoterCreationForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ('personal_id','votekey' , 'region')
    
    def save(self, commit=True):
        user = super(VoterCreationForm, self).save(commit=False)
        votekey = self.cleaned_data['votekey']
        user.set_password(votekey)
        if commit:
            user.save()
        return user

class VoterChangeForm(UserChangeForm):
# to be changed 
    class Meta:
        model = Voter
        fields = ('personal_id','votekey' , 'region' )