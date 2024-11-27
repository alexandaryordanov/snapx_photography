from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from snapxPhotography.common.models import Vote
from snapxPhotography.photos.models import Photo
from snapxPhotography.common.serializers import PhotoSerializer, VoteSerializer


# Create your views here.
class PhotoAddPageView(CreateView):
    pass


class PhotoDeletePageView(DeleteView):
    pass


class VotePhotoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk: int):
        try:
            photo = Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            return Response({"detail": "Photo not found."}, status=status.HTTP_404_NOT_FOUND)

        if Vote.objects.filter(user=request.user, photo=photo).exists():
            return Response({"detail": "You have already voted for this photo."}, status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(user=request.user, photo=photo)

        photo.vote += 1
        photo.save()

        return Response({"message": "Vote added successfully", "votes": photo.vote}, status=status.HTTP_200_OK)
