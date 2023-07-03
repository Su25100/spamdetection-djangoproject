from rest_framework import serializers
from .models import Phonenumber , User, Contact

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phonenumber
        fields=['id','name','is_spam','phone_no']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone_no']

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = User
        fields = ['name', 'phone_no', 'email', 'contacts']
