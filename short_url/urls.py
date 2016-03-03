"""short_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from short_url_app.views import BookmarkListView, BookmarkCreateView,\
    BookmarkUpdateView, external_view, HomeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^bookmarks/$', BookmarkListView.as_view(), name='bookmark_list_view'),
    url(r'^bookmark/create/$', BookmarkCreateView.as_view(), name='bookmark_create_view'),
    url(r'^bookmark/update/(?P<pk>\d+)$', BookmarkUpdateView.as_view(), name='bookmark_update_view'),
    url(r'^/b/(?P<short>\w+)', external_view, name='external_view')
]
