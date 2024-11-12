from django.urls import path, include
from snapxPhotography.photos import views

urlpatterns = [
    path('add/', views.PhotoAddPageView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditPageView.as_view(), name='photo-edit'),
        path('delete/', views.PhotoDeletePageView.as_view(), name='photo-delete'),
    ])),
]
