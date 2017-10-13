from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from api import views
from django.contrib.auth import views as auth_views

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/login'}, name='logout'),
    url(r'^moviestore/$', CreateView.as_view(), name="create"),
    url(r'^moviestore/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^home/$', views.IndexPageView.as_view(), name='home'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
