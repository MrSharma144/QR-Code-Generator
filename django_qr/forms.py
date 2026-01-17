from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        label='Restaurant Name',
         max_length=100,
         widget=forms.TextInput(attrs={
                'placeholder': 'Enter the name of the restaurant',
                'class': 'form-control',
            })
         )
    url = forms.URLField(
        label='Menu URL',
          max_length=200,
          widget=forms.URLInput(attrs={
                'placeholder': 'Enter the URL of the menu',
                'class': 'form-control',
            })
    )
