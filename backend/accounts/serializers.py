from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password         = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = [
            'email', 'first_name', 'last_name',
            'niveau',  'specialite',                         
            'password', 'password_confirm'
        ]

    def validate_niveau(self, value):
        valid = [choice[0] for choice in User.NiveauScolaire.choices]
        if value and value not in valid:
            raise serializers.ValidationError("Niveau scolaire invalide.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    full_name     = serializers.SerializerMethodField()
    niveau_label  = serializers.SerializerMethodField()   # ← label lisible

    class Meta:
        model  = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'full_name', 'niveau', 'niveau_label', 
            'specialite',
            'created_at'
        ]
        read_only_fields = ['id', 'email', 'created_at']

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_niveau_label(self, obj):
        return obj.get_niveau_display() if obj.niveau else None