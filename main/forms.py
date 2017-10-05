from django import forms


class PickupForm(forms.Form):
    pickup_time = forms.TimeField(label="Prise en charge d'un rendez-vous prévu à", label_suffix=' : ', required=True)
