from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "some placeholder text",
            }
        )
    )  # by default, required=True
    description = forms.CharField(
        label="",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 20,
                "cols": 128,
            }
        ),
    )  # make the label blank
    price = forms.DecimalField(initial=199.99)  # initial value
