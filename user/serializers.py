from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)  # Champ pour la confirmation du mot de passe

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password_confirm', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')  # Retirer le champ de confirmation avant de créer l'utilisateur
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("User does not exist")
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        data["user"] = user  # Assurez-vous que vous renvoyez l'utilisateur sous la clé 'user'
        return data
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'first_name', 'last_name']