from rest_framework import serializers
from files.models import File

class FileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = File
        fields = ['id', 'file', 'user', 'created_at', 'name']

