from django import forms
from .models import User, Equacao

#model form
class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'nome', 
            'telefone',
            'email'
        ]


class EquacaoForm (forms.ModelForm):
    class Meta:
        model = Equacao
        fields = [
            'a',
            'b',
            'c'
        ]
        
