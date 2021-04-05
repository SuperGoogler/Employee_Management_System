from rest_framework import serializers
from .models import NewEmployeeProfile
from django.contrib.auth.hashers import make_password


class RegistrationSerializers(serializers.ModelSerializer):
    '''
    We need to add the password2, as its not the part of the NewEmployeeProfile model. So, we need to make it manually.
    '''
    password2 = serializers.CharField(style={'input_type: password'}, write_only=True)

    class Meta:
        model = NewEmployeeProfile
        fields = ('email', 'first_name', 'last_name', 'employee_code', 'contact', 'dob', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def create(self, validated_data):
    #     """
    #     before we save the new user, we need to make sure that the password1, and password2 matches. In order to do
    #     that, we need to override the save() method.
    #     """
    #
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #
    #     if password != password2:
    #         raise serializers.ValidationError({'password': f'password must match..'})
    #         return
    #         #return NewEmployeeProfile.objects.create(**validated_data)
    #
    # def validate(self, attrs):
    #     if attrs:
    #         account = NewEmployeeProfile(
    #             email=self.validated_data['email'],
    #             first_name=self.validated_data['first_name'],
    #             last_name=self.validated_data['last_name'],
    #             employee_code=self.validated_data['employee_code'],
    #             contact=self.validated_data['contact'],
    #             dob=self.validated_data['dob'],
    #         )
    #         account.save()
    #         return account

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        super().create(validated_data)

    def validate(self, attrs):
        if attrs.get("password") != attrs.pop("password2"):
            raise serializers.ValidationError({"password": f"password must match.."})
        return super().validate(attrs)
