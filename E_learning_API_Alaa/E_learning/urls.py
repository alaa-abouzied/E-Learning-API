from django.contrib import admin
from django.urls import include, path
from elearning import views
from elearning.views import *
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
router = DefaultRouter()
router.register('guests',views.viewsets_guest)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('elearning/', include("elearning.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

