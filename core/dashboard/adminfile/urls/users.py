from django.urls import path
from .. import views



urlpatterns = [
    path('users-list/',views.AdminUserListView.as_view(),name='users-list'),
    path('users/<int:pk>/edit/',views.AdminUserUpdateView.as_view(),name='users-edit'),
    path('users/<int:pk>/delete/',views.AdminUserDeleteView.as_view(),name='users-delete')

]