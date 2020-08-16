from dataclasses import field

from rest_framework import serializers
from .models import CustomUser


class CustomUserModelSearializers ( serializers.ModelSerializer ):
    """
    Serializers to Model CustomUser
    """

    password = serializers.CharField( max_length=128,
                                      style={'input_type':'password'})

    confirm_password = serializers.CharField( max_length=128,
                                             style={'input_type':'password'},
                                             write_only=True )
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name','last_name','email',
                  'username','date_of_birth','contact_number',
                  'contact_address','password','confirm_password',]


    @staticmethod
    def validate_contact_number( contact_number ):
        """
        Validate the contact number field
        """
        if len( str( contact_number ) ) != 10:
            raise serializers.ValidationError("Invalid Contact Number. Your Number should be of 10 digits")
        return contact_number

    def validate(self,data):
        """
        Checks if the password and confirm password matches
        :param data: dictionary key,value from field,submitted data
        :return data without confirm_password key in dictionary:
        """
        password = data['password']
        confirm_password = data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError("password do not match")
        else:
            # Popping out confirm_password key,value as there is no attribute in model to save
            _ = data.pop('confirm_password')
        return data

    def create(self, validated_data):
        """
        Overriding create class to set hashable password of user
        :return: instance of the CustomUser
        """
        password = validated_data['password']
        user = super( CustomUserModelSearializers, self ).create( validated_data )
        user.set_password( password )           # converting to hashable password
        user.save()
        return user

    def update(self, instance, validated_data):
        """
            Overriding update class to set hashable password of user
            :return: instance of the CustomUser
        """
        password = validated_data [ 'password' ]
        user = super( CustomUserModelSearializers, self ).update( instance,validated_data )
        user.set_password( password )  # converting to hashable password
        user.save()
        return user


