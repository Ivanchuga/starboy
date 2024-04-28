from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name="shop"

urlpatterns = [
    path("", views.all_items, name="all_items"),
    path('<int:book_id>/', views.single_quote, name="single_book"),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)