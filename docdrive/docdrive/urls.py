from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
