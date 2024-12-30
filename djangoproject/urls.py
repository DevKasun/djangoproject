from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url="articles/")), # This will Redirect / to the articles page
    path('__debug__/', include('debug_toolbar.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
