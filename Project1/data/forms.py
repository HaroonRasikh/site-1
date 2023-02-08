from django import forms
class contactusForm(forms.Form):
    Name = forms.CharField(max_length=25,required=True)
    Email = forms.EmailField(required=True)
    #subject = forms.CharField(required=True)
    Message = forms.CharField(widget=forms.Textarea,required=True)

class subscribForm(forms.Form):
    subscrib= forms.CharField(max_length=25,required=True)
    Email = forms.EmailField(required=True)