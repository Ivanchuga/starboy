from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name= "quotes"

urlpatterns = [
    path('', views.all_quotes, name="all_quotes"),
    path('<int:quote_id>/', views.single_quote, name="single_quote"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
