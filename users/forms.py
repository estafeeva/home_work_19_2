from users.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

