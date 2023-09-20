from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('petsall/',views.petsall,name='petsall'),
    path('petsall/petsdetails/<int:id>',views.petsdetails,name='petsdetails'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
