"""django_rest_expenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


main_urls = [
    path('users/', include('users.urls')),
    path('costs/', include('expenses.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(main_urls)),
    # path('api/', include('expenses.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]


# main_urls = [
#     # path('users/', include('users.urls')),
#     # path('costs/', include('expenses.urls')),
# ]
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('expenses.urls')),
#     # path('api/', include(main_urls)),
#
#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#     # url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
# ]

