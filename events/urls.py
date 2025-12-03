from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("<int:pk>/", views.event_detail, name="event_detail"),
    path("new/", views.event_create, name="event_create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
