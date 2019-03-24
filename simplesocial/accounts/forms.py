from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# object name should not be the same name of parent
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        # get current model of user currently using website
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # sets a custom label for a form field
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"
