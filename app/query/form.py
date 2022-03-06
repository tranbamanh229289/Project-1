from django import forms

class PostForm (forms.Form):
    query = forms.CharField(label="",max_length=100, required=True);