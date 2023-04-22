from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"


urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('dashboard/<input>',views.dashboard_new,name = "dashboard_new"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('addsongpop/',views.addSongPop,name = "addsongpop"),
    path('addsongdangdut/',views.addSongDangdut,name = "addsongdangdut"),
    path('addsongmanca/',views.addSongManca,name = "addsongmanca"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('songupdate/<int:id>',views.updateSong,name = "songupdate"),
    path('medsosupdate/<int:id>',views.updateMedsos,name = "medsosupdate"),    
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('songdelete/<int:id>',views.deleteSong,name = "songdelete"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
]
