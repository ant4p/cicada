"""
URL configuration for cicada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cicada import settings
from src.views import ShowRobotsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.urls', namespace='src')),
    path('services/', include('services.urls', namespace='services')),
    path('products/', include('products.urls', namespace='products')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('tags/', include('tags.urls', namespace='tags')),
    path('robots.txt', ShowRobotsView.as_view(content_type='text/plain'), name='robots'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]


admin.site.site_header = 'Панель управления'
admin.site.index_title = 'CICADA 3D'