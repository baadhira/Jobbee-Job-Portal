from django.urls import path
from .import views

urlpatterns =[
    path('jobs/',views.getAllJobs,name='jobs'),
    path('jobs/new/',views.newJob,name='newJob'),
    path('jobs/<int:pk>/',views.getJob,name='job'),
    path('jobs/<int:pk>/update/',views.updataJob,name='updataJob'),
    path('jobs/<int:pk>/delete/',views.delete_job,name='delete_job'),
    path('stats/<str:topic>/',views.getTopicStats,name='getTopicStats'),
    path('jobs/<int:pk>/apply/',views.applyToJob,name='applyToJob'),
    path('me/jobs/applied/',views.getCurrentUserAppliedJobs,name='getCurrentUserAppliedJobs'),
    path('me/jobs/',views.getCurrentUserJobs,name='getCurrentUserJobs'),

    path('jobs/<int:pk>/check',views.isApplied,name='isApplied'),
    path('jobs/<int:pk>/candidates/',views.getCandidatesApplied,name='getCandidatesApplied'),


]