from rest_framework.serializers import ModelSerializer
from .model import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=[
            'name'
        ]
