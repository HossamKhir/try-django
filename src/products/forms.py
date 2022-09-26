from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "some placeholder text",
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 20,
                "cols": 128,
            }
        ),
    )
    price = forms.DecimalField(initial=199.99)
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" not in title:
            raise forms.ValidationError("This is not a valid title!")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid e-mail")
        return email


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
