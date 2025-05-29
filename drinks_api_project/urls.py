from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from drinks_api.views import DrinkViewSet, home  # ✅ view home

# ✅ Router cho API
router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='drink')  # => /api/drinks/

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏠 Trang chủ
    path('', home, name='home'),

    # 📱 API đồ uống
    path('api/', include(router.urls)),

    # 🔐 JWT Token (nếu dùng)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔐 Django auth URLs (login/logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # 🧩 Include URL trong app (nếu có các trang riêng như login, admin page,...)
    path('', include('drinks_api.urls')),

    # 🔗 Favicon
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

# 🖼️ Static/media trong dev mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
