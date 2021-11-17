from ca.api.views import  DonCreateApiView, DonateurCreateApiView, DonateurDetail, DonateurListAPIView, DonsListAPIView, PromesseCreateApiView, PromesseDonsListAPIView
from django.urls import path
from . import views
 
#from news.api.views import (article_detail_api_view, 
 #                           article_list_create_api_view)
 


urlpatterns = [
  
  path('',DonateurListAPIView.as_view(), name="donateur-list"),
  # path('dashboard', views.dashboardview),
  path('dons',DonsListAPIView.as_view(), name="dons-list"),
  path('dons/add/', DonCreateApiView.as_view(), name='dons-add'),
  
  # path('', DonateurListView.as_view(), name='donateur-list'),
  path('donateur/add/', DonateurCreateApiView.as_view(), name='donateur-add'),
  # path("article/",ArticleListCreateAPIView.as_view(), name="article-list"),
    
  path("donateur/<int:pk>/",DonateurDetail.as_view(), name="donateur-detail"),
  path('promesse',PromesseDonsListAPIView.as_view(), name="promesse-list"),
  path('promesse/add/', PromesseCreateApiView.as_view(), name='promesse-add'),

    
  #   path("journalist/",JournalistListCreateApiiView.as_view(), name="journalist-list"),
#    path("article/", article_list_create_api_view, name="article-list"),
#    path("article/<int:pk>/",article_detail_api_view, name="article-detail")

]