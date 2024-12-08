from django.urls import path, include
from snapxPhotography.contests import views

urlpatterns = [
    path('', views.ContestsDashboardView.as_view(), name='contest-dashboard'),
    path('add/', views.ContestAddPageView.as_view(), name='contest-add'),
    path('<int:pk>/', include([
        path('', views.ContestDetailsView.as_view(), name='contest-details'),
        path('delete/', views.ContestDeletePageView.as_view(), name='contest-delete'),
    ])),
]