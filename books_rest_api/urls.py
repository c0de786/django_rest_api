from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import GetAllBooks
from .views import UserView
from .views import UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = {
    url(r'^all/',GetAllBooks.as_view(), name="all"),
    url(r'^booklists/$', CreateView.as_view(), name="create"),
    url(r'^booklists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token), # Add this line
    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)