from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^login_page/', views.login_page)
]
app_name = 'blog'
