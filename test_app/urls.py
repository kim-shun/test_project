from django.urls import path
from . import views

app_name = 'test_app'
urlpatterns = [
    #path('',views.IndexView.as_view(),name="index"),
    path('',views.hoge_a,name="hoge_a"),
    path('users/',views.users,name="users"),
]
