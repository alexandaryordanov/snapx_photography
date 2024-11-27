from rest_framework import serializers

from snapxPhotography.common.models import Vote
from snapxPhotography.photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'title', 'description', 'image', 'uploaded_at', 'votes', 'uploaded_by', 'contest']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'photo', 'created_at']
