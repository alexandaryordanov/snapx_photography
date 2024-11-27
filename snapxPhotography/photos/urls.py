from django.urls import path, include
from snapxPhotography.photos import views
from snapxPhotography.photos.views import VotePhotoView

urlpatterns = [
    path('add/', views.PhotoAddPageView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('delete/', views.PhotoDeletePageView.as_view(), name='photo-delete'),
        path('vote/', VotePhotoView.as_view(), name='photo-vote'),
    ])),
]
