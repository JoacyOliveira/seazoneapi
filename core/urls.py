from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from seazone.api.viewsets import Check_ViewSet,Limpeza_ViewSet

router = routers.DefaultRouter()
router.register(r'seazone', Check_ViewSet),\
router.register(r'limpeza', Limpeza_ViewSet),

urlpatterns = [
    path('api/',include(router.urls)),
    path('', admin.site.urls),

]
