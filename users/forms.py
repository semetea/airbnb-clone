from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # if you want to valid the field, you should define function name like clean_[field name]
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                # should return cleaned_data when you clean function
                return self.cleaned_data
            else:
                # make error belongs to password
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            # make error belongs to email, if you divide clean function, you can just use raise
            self.add_error("email", forms.ValidationError("User does not exist"))
