from django.contrib.auth.views import LoginView

from accounts.form import LoginForm

# Create your views here.


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm
