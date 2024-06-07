from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('koss/', admin.site.urls),
    path('', include('Blog.crispy_kitchen.urls')),
    path('accounts/', include('Blog.accounts.urls')),
    path('blog/', include('Blog.crispy_blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
