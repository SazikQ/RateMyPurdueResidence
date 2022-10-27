from django.urls import path
from . import views
#from .views import EditProfileView
from django.views.generic import TemplateView

from .views import ReviewHistoryView, ReviewDetail

urlpatterns = [
    path('', views.profile, name = "profile"),
    path('edit/', views.edit_profile, name = "editProfile"),
    path('verify/', views.account_verify, name = "verifyUser"),
    path('past_review_list/', ReviewHistoryView.as_view(), name='past_review'),
    path('past_review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]