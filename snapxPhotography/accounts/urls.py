from django.contrib.auth.views import LogoutView
from django.urls import path, include
from snapxPhotography.accounts import views

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/<int:pk>/', include([
        path('', views.AccountDetailView.as_view(), name='account-details'),
        path('edit/', views.AccountEditView.as_view(), name='account-edit'),
        path('delete/', views.AccountDeleteView.as_view(), name='account-delete'),
    ]))
]