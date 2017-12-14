from django import forms

class TreasureForm(forms.Form):
    name = forms.CharField(label='Name',max_length=50)
    value = forms.DecimalField(label='Value',max_digits=10, decimal_places=2)
    location = forms.CharField(max_length=50,label='location')
    img_url = forms.CharField(max_length=100,label='Image URL')