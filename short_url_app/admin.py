from django.contrib import admin
from short_url_app.models import Bookmark, Click

admin.site.register([Bookmark, Click])
