from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User

from short_url_app.models import Bookmark, Click
from hashids import Hashids


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ('url', 'title', 'description')

    def form_valid(self, form):
        object = form.save(commit=False)
        hashids = Hashids(min_length=5)
        object.user = self.request.user
        object.save()
        object.shortened = hashids.encode(object.pk)
        object.save()
        Click.objects.create(bookmark=object)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookmark_list_view')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ('url', 'title', 'description')
    template_name = 'short_url_app/update_form.html'

    def get_success_url(self):
        return reverse('bookmark_list_view')


def home(request):
    return render(request, 'base.html')

def external_view(request, short):
    bookmark = Bookmark.objects.get(shortened=short)
    click = Click.objects.get(bookmark=bookmark)
    click.last_accessed = datetime.now()
    click.access_count += 1
    click.save()

    return HttpResponseRedirect(bookmark.url)