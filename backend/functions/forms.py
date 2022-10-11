from email.policy import default
from pickle import FALSE
from django import forms
from backend.user_profile.models import Review


class ResidenceForm(forms.Form):
    name = forms.CharField(label='Residence name', max_length=100)
    streetName = forms.CharField(max_length=100)
    streetNum = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=6)

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=500)
    isAnonymous = forms.BooleanField(label = "Post Anonymously?", initial=False, required=False)
    # class Meta:
    #     model = Review
    #     fields = ('title', 'content')

    #     widgets = {
    #         'title': forms.TextInput(),
    #         'content': forms.Textarea(),
    #     }