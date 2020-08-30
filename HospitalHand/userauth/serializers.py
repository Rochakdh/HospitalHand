from dataclasses import field

from rest_framework import serializers
from .models import CustomUser



class CustomUserModelSignUpSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128,
                                             style={'input_type': 'password'},
                                             write_only=True)
    password = serializers.CharField(max_length=128,
                                             style={'input_type': 'password'},
                                             write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email','username', 'contact_number','password', 'confirm_password']
        read_only_fields=['id']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @staticmethod
    def validate_contact_number( contact_number ):
        """
        Validate the contact number field
        """
        if contact_number is None:
            raise serializers.ValidationError("Enter your Contact Number")

        if len( str( contact_number ) ) != 10:
            raise serializers.ValidationError("Contact Number should be of 10 digits")
        return contact_number

    def validate(self,data):
        """
        Checks if the password and confirm password matches
        :param data: dictionary key,value from field,submitted data
        :return data without confirm_password key in dictionary:
        """
        # view = self.context.get('view')
        # print(view)
        # if view and view.action == 'create':
        password = data['password']
        confirm_password = data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError("password do not match")
        else:
            # Popping out confirm_password key,value as there is no attribute in model to save
            _ = data.pop('confirm_password')
        return data
        # return super().validate(data)

    def create(self, validated_data):
        """
        Overriding create class to set hashable password of user
        :return: instance of the CustomUser
        """
        password = validated_data['password']
        user = super( CustomUserModelSignUpSerializers, self ).create( validated_data )
        user.set_password( password )           # converting to hashable password
        user.save()
        return user




class CustomUserModelSerializers ( serializers.ModelSerializer ):
    """
    Serializers to Model CustomUser
    """

    old_password = serializers.CharField( max_length=128,
                                             style={'input_type':'password'},
                                             write_only=True )
    new_password = serializers.CharField(max_length=128,
                                         style={'input_type': 'password'},
                                         write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email',
                  'username','contact_number','contact_address','new_password','old_password'
                  ,'first_name','middle_name','last_name','date_of_birth','profile_pictures']
        read_only_fields = ['id']
        extra_kwargs = {
            'password':{
                'write_only' : True
            },
        }


    @staticmethod
    def validate_contact_number( contact_number ):
        """
        Validate the contact number field
        """
        if contact_number is None:
            raise serializers.ValidationError("Enter your Contact Number")

        if len( str( contact_number ) ) != 10:
            raise serializers.ValidationError("Contact Number should be of 10 digits")
        return contact_number

    def validate(self,data):
        """
        Checks if the password and confirm password matches
        :param data: dictionary key,value from field,submitted data
        :return data without confirm_password key in dictionary:
        """
        view = self.context.get('view')
        if view and view.action == 'create':
            password = data['password']
            confirm_password = data['confirm_password']
            if password != confirm_password:
                raise serializers.ValidationError("password do not match")
            else:
                # Popping out confirm_password key,value as there is no attribute in model to save
                _ = data.pop('confirm_password')
            return data
        return super().validate(data)

    # def create(self, validated_data):
    #     """
    #     Overriding create class to set hashable password of user
    #     :return: instance of the CustomUser
    #     """
    #     password = validated_data['password']
    #     user = super( CustomUserModelSerializers, self ).create( validated_data )
    #     user.set_password( password )           # converting to hashable password
    #     user.save()
    #     return user

    def update(self, instance, validated_data):
        """
            Overriding update class to set hashable password of user
            :return: instance of the CustomUser
        """
        print(f'VAlDATED{validated_data}')
        user = super(CustomUserModelSerializers, self).update(instance,validated_data)
        if validated_data.get("old_password"):
            if not user.check_password(validated_data.get("old_password")):
                raise serializers.ValidationError('Old Password Not Correct')
            password = validated_data['new_password']
            user.set_password(password)  # converting to hashable password
        user.save()
        return user
