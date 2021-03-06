from django.contrib.auth.models import User, Group
from .models import ProofOfConcept
from rest_framework import serializers
from .fields import Base64ImageField


class ProofSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = ProofOfConcept
        fields = ('name', 'data', 'image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


