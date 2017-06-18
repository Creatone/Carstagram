from django.conf.urls import url

from carstagram import views

app_name = 'carstagram'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^register/$',views.UserFormView.as_view(), name='register')
]