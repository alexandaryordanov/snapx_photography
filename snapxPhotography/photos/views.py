from django.http import request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from snapxPhotography.common.models import Vote
from snapxPhotography.contests.models import Contest
from snapxPhotography.photos.forms import PhotoAddForm
from snapxPhotography.photos.models import Photo
from snapxPhotography.common.serializers import PhotoSerializer, VoteSerializer


# Create your views here.
class PhotoAddPageView(CreateView):
    template_name = 'photos/add_photo.html'
    model = Photo
    form_class = PhotoAddForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        contest_name = self.request.GET.get('current_contest')
        if contest_name:
            contest = get_object_or_404(Contest, name=contest_name)

            kwargs['initial'] = {'contest': contest}

        return kwargs

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.uploaded_by = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contest-details', kwargs={'pk': self.object.contest.pk})


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
