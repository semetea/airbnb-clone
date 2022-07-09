from django.views import View
from django.shortcuts import render
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "taewooocean@naver.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form})


# same thing as below
# def login_view(request):
#     if request.method == "GET":
#         pass

#     if request.method == "POST":
#         pass
