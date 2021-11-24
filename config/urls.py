from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

# API
urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]
