from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
        "required": "Your name must not be empty!",
        "max_length":"Pleae enter a shorter name!"
    })