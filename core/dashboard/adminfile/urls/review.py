from django.urls import path
from .. import views



urlpatterns = [
    path('review-list/',views.AdminReviewListView.as_view(),name='review-list'),
    path('review/<int:pk>/edit/',views.AdminReviewEditView.as_view(),name='review-edit'),
    path('review/<int:pk>/invoice/',views.AdminReviewDeleteview.as_view(),name='review-delete'),

]
