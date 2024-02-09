from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import movie_list,movie_details
from .views import WatchListAV , WatchDetailAV , StreamPlatformAV ,StreamPlatformDetailAV


urlpatterns = [
    path('list/',WatchListAV.as_view() , name="watch-list"),
    path('<int:pk>/',WatchDetailAV.as_view() , name="watch-details"),
    path('stream/',StreamPlatformAV.as_view() , name="stream-platform"),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view() , name="streamplatform-detail")
]