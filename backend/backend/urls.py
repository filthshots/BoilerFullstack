from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from backend.views import FacebookLogin
from django.views.generic import TemplateView, RedirectView
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns = [
    # Admin view
    url(r'^admin/', admin.site.urls),

    # Rest auth api
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # Social Accounts
    url(r'^rest-auth/facebook/connect/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),

    # Allauth views
    url(r'^account/', include('allauth.urls')),

    # Redirect View
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),

    # Views that require a frontend connection
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^user-details/$', TemplateView.as_view(template_name="user_details.html"), name='user-details'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"), name='logout'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"), name='login'),
    url(r'^password-reset/confirm/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password-reset-confirm'),
    url(r'^password-reset/$', TemplateView.as_view(template_name="password_reset.html"), name='password-reset'),
    url(r'^password-change/$', TemplateView.as_view(template_name="password_change.html"), name='password-change'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^email-verification/$', TemplateView.as_view(template_name="email_verification.html"), name='email-verification'),
    url(r'^email-verification/$', TemplateView.as_view(template_name="email_verification.html"), name='email-verification'),
]
