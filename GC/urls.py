from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    #path('dashboardc', views.dashboardc, name='dashboardc'),
    #path('viewcc', views.viewcc, name='viewcc'),
    path('addcc', views.addcc, name='addcc'),
    path('logout', views.logout, name='logout'),

    #path('dashboarda', views.dashboarda, name='dashboarda'),
    path('logout', views.logout, name='logout'),

    path('dashboarda', views.home,name='home'),
    path('pendingcomplaints/', views.pendingcomplaintslisting, name="pendingcomplaintslisting"),
    path('viewuser/', views.viewuser, name="viewuser"),
    path('complaints/', views.complaintslisting, name="complaintslisting"),
    path('usercomplaints/', views.viewcomplaint, name="viewcomplaint"),
   
    path('addcomplaint/', views.addcomplaint, name="addcomplaint"),
    path('complaintinserted/', views.complaintinserted, name="complaintinserted"),
    path('editpending/<int:id>',views.updateform,name="updateform"),
    path('complaintupdate/',views.complaintupdate,name="complaintupdate")


]