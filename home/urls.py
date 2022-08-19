from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="PRASANT RAJ"
admin.site.site_title="Welcome to prasant's dashboard"
admin.site.index_title="welcome to this portal"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact')

]