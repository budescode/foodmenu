"""foodmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index, About, Order, Menu, MenuSearch
from restaurant.views import Signup

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
		path('accounts/', include('django.contrib.auth.urls')),
		path('restaurant/', include('restaurant.urls')),
		path('signup/', Signup.as_view(), name='signup'),
		path('', Index.as_view(), name='index'),
		path('about/', About.as_view(), name='about'),	
		path('menu', Menu.as_view(), name='menu'),
		path('menu/search', MenuSearch.as_view(), name='menu-search'),
		path('order/', Order.as_view(), name='order'),
		#path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation'),
		url(r'^media/(?P<path>.*)$', serve,{'document_root':			settings.MEDIA_ROOT}),
		url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
