from django.urls import path, include
from snapxPhotography.categories import views

urlpatterns = [
    path('', views.CategoryDashboardView.as_view(), name='category-dashboard'),
    path('add/', views.CategoryAddPageView.as_view(), name='category-add'),
    path('<int:pk>/', include([
        path('', views.CategoryDetailsView.as_view(), name='category-details'),
        path('edit/', views.CategoryEditPageView.as_view(), name='category-edit'),
        path('delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    ])),
]