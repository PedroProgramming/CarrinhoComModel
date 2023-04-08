from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrinho/', include('carrinho.urls')),
    path('home/', include('home.urls')),
    path('', lambda request: redirect('/home/'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)