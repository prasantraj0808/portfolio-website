from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="PRASANT RAJ"
admin.site.site_title="Welcome to prasant's dashboard"
admin.site.index_title="welcome to this portal"


from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]