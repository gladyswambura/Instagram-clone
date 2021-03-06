from django.urls import path, re_path
from . import views
from .views import index, NewPost, PostDetail,like, favourite
from . import views as app_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # PROFILE SECTION
    path('profile/',views.profile,name='profile'),
    path('profile/update/',app_views.update_profile,name='update_profile'),
    re_path(r'^new/profile$', views.add_profile, name='new_profile'),

    # MAIN PAGE && POST SECTION
    path('', views.index, name='index'),
    path('newpost', app_views.NewPost, name='newpost'),
    path('post/<int:pk>/', views.PostDetail, name='post-detail'),
    re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)/',views.like, name='like'),
    re_path(r'^all/(?P<pk>\d+)', views.all, name='all'),
    path('addcomment//',views.addComment,name='addcomment'),
    # path('comment/', views.new_comment, name='comment'),
    re_path(r'^search/', views.search_results, name='search_results'),
    path('comment/', views.comment, name='comment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)