from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('view/WTq8zYcZfaWVvMncigHqwQ<str:code>WTq8zYcZfa<slug:expiredt>WVvMncigHqwQ', views.view, name='view'),
    path('thankyou', views.thanks, name='thanks'),
    path('error', views.error, name='error'),
    path('verify', views.handleRedeemCode, name="handleRedeemCode"),
]
urlpatterns += staticfiles_urlpatterns()
