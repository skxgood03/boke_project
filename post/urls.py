from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.all,name = 'all' ),
    path('page/<int:num>',views.all,name = 'all' ),
    path('posts/<int:num>',views.allpost,name = 'allpost' ),
    path('category/<int:cid>',views.postid,name = 'postid' ),
    path('archive/<int:month>/<int:year>',views.PostCreated ),
]