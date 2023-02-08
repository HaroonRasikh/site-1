from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('1',views.hesab,name='hesab'),
    path('hesabat/<str:pk>',views.Hesabpost,name='hesabat'),
    path('2',views.ugur,name='ugur'),
    path('heykaye/<str:pk>',views.Ugurapost,name='heykaye'),
    path('contact',views.contact, name = 'contact'),


    path('anlayışlar',views.agreement, name='agreement'),
    
    path('3',views.maqala, name = 'maqala'),
    path('maqala/<str:pk>',views.maqalapost,name='maqala'),
    path('resurs/<str:pk>',views.resurspost,name='resurs'),
    
    
    path('4',views.resource, name = 'resource'),
    path('login', views.Login, name = 'login'), 
    path('',views.Home, name = 'anasahifa'),
    path('Haqqimda',views.about,name='hakkimda'),
    path('Xidmatlar',views.Service, name = 'xidmalar'),
    path('İş',views.Work, name = 'iş'),
    path('Komanda',views.komanda, name='komanda'),
    path('komandamiz/<str:pk>',views.komandapost,name='komandamiz'),
    path('elaqe',views.alaqa,name = 'elaqe'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='forget.password.html'),name='reset_password'),

path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='yenişifre.html'),name='password_reset_confirm'),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),


]
