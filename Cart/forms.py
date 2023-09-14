from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=False, label='Кол-во: ', initial=1, widget=forms.TextInput)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)