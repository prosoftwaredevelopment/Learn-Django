from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject Description',min_length=1,widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    