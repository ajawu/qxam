from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'onxam_app'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('dummy/', views.dummy_page, name='dummy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
