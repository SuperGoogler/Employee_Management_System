from django.contrib.auth.forms import UserCreationForm, get_user_model, forms
#from .models import NewEmployeeProfile


class NewUserCreateForm(UserCreationForm):
    contact = forms.CharField(max_length=10)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'employee_code', 'dob')
        labels = {'contact': 'mobile_number', }