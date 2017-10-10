from django import forms


class PickupForm(forms.Form):
    scheduled_time = forms.TimeField(label="Prise en charge d'un rendez-vous prévu à", label_suffix=' : ', required=True)


class LoginForm(forms.Form):
    password = forms.CharField(label="Mot de passe", label_suffix=' : ', required=True, strip=True)
