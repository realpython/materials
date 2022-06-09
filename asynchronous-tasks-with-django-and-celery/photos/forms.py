from django import forms


class PhotoFetchForm(forms.Form):
    number_of_images_to_fetch = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={"style": "width:6ch", "min": "1"}),
    )
