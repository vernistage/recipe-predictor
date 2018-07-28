"""forms for Welcome app."""

from django import forms


class WelcomeForm(forms.Form):
    """Capture user name to display on welcome page."""

    your_name = forms.CharField(label='Input your name', max_length=100)
