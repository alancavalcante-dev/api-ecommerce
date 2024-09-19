from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from logs.views import LogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LogsView.as_view(), name='ok'),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('sellers.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('reviews.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
