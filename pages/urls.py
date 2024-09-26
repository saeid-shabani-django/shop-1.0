from django.urls import path

from . import views


urlpatterns = [
    path('about/',views.AboutUsView.as_view(),name='about'),
    path('',views.HomePageView.as_view(),name='home'),

]