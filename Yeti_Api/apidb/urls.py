from django.urls import path

from .views import LogView, RegView, ProfileView, TimelineView

app_name = "apidb"

urlpatterns = [
    path('user/log/', LogView.as_view()),
    path('user/reg/', RegView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
    path('events/', TimelineView.as_view()),
]