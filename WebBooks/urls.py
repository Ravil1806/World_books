from django.urls import path, include
from django.contrib import admin
from catalog import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(),
        name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(),
        name='authors')
]
urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]
urlpatterns += [url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(),
                    name='my-borrowed')]

