from django.conf.urls import patterns, url
from dragon import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^Login/$', views.user_login, name='login'),
        url(r'^Login/userHome', views.userHome, name='userHome'),
        url(r'^Login/userinfo', views.user_info, name='user_info'),
        url(r'^Login/info/(\d{1,2})/$', views.user_info1, name='user_info1'),
        url(r'^Login/viewList', views.user_available, name='user_available'),
        url(r'^Login/ownedList', views.user_ExperListNow, name='user_ExperListNow'),
        url(r'^Login/ownList/(\d{1,2})/$', views.user_ExperOne, name='user_ExperOne'),
        url(r'^Login/offer/(\d{1,2})/$', views.user_offer, name='user_offer'),
        url(r'^Login/refuse/(\d{1,2})/$', views.user_refuse, name='user_refuse'),
        url(r'^Login/cancel/(\d{1,2})/$', views.user_cancel, name='user_cancel'),
        url(r'^Login/addNewExperiment/$', views.addNewExperiment, name='add_NewExperiment'),
        url(r'^Login/applyList', views.user_ApplyListNow, name='user_ApplyListNow'),
        url(r'^Login/pending/(\d{1,2})/$', views.user_pCancel, name='user_pCancel'),
        url(r'^Login/invited/accept/(\d{1,2})/$', views.user_iAccept, name='user_iAccept'),
        url(r'^Login/invited/reject/(\d{1,2})/$', views.user_iReject, name='user_iReject'),
        url(r'^Login/apply/(\d{1,2})/$', views.apply_intro_login, name='apply_intro_login'),
        url(r'^Login/intro/(\d{1,2})/$', views.intro_login, name='intro_login'),
        url(r'^Login/intro/apply', views.user_Apply, name='user_Apply'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^search/$', views.index_search, name='search'),
        url(r'^intro/(\d{1,2})/$', views.intro_out, name='intro')
         )