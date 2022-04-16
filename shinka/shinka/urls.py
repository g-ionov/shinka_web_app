from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from .yasg import urlpatterns as doc_urls
from shinka import settings

urlpatterns = [
    path('djadmin_shinka/', admin.site.urls),
    path('api/v1/shinka_app/', include('shinka_app.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    # path('api/token/verify/', TokenVerifyView.as_view()),

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]

urlpatterns += doc_urls

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)