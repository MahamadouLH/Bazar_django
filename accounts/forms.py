from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'Entrez votre mot de passe',
            'autocomplete' : 'none',
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder' : 'Confirmer le mot de passe',
            'autocomplete' : 'none',
        }
    ))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password :
            raise forms.ValidationError("les mots de passes ne sont pas conformes...")
    
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__( *args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Votre prénom'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Votre nom'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Votre numéro de téléphone'
        self.fields['email'].widget.attrs['placeholder'] = 'Votre adresse mail'
        self.fields['email'].widget.attrs['autocomplete'] = 'none'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    