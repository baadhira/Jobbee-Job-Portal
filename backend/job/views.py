from rest_framework.decorators import api_view,permission_classes
from .models import CandidateApplied,Job
from rest_framework.permissions import IsAuthenticated
from .serializers import JobSerializer,CandidatesAppliedSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Avg,Min,Max,Count
from .filters import JobFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllJobs(request):
    filterset=JobFilter(request.GET,queryset=Job.objects.all().order_by('id'))
    count=filterset.qs.count()
    # jobs=Job.objects.all()
    resPerPage=3
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage

    querysets=paginator.paginate_queryset(filterset.qs,request)

    serializer=JobSerializer(querysets,many=True)
    return Response({
        "count":count,
        "resPerPage":resPerPage,
        "jobs":serializer.data
        })

@api_view(['GET'])
def getJob(request,pk):
    # print(pk)
    job=get_object_or_404(Job,id=int(pk))

    candidates=job.candidateapplied_set.all().count()
    serializer=JobSerializer(job,many=False)

    return Response({'job':serializer.data,'candidates':candidates})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newJob(request):
    request.data['user'] = request.user
    data=request.data
    job=Job.objects.create(**data)
    serializer=JobSerializer(job,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updataJob(request,pk):
    job=get_object_or_404(Job,id=pk)

    if job.user != request.user:
        return Response({'message':'You cannot update this job'},status=status.HTTP_403_FORBIDDEN)

    job.title=request.data['title']
    job.description=request.data['description']
    job.email=request.data['email']
    job.address=request.data['address']
    job.jobType=request.data['jobType']
    job.education=request.data['education']
    job.industry=request.data['industry']
    job.experience=request.data['experience']
    job.salary=request.data['salary']
    job.positions=request.data['positions']
    job.company=request.data['company']
    job.save()



    serializer=JobSerializer(job,many=False)

    return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def delete_job(request,pk):

    job=get_object_or_404(Job,id=pk)

    if job.user != request.user:
        return Response({'message':'You cannot delete this job'},status=status.HTTP_403_FORBIDDEN)
    job.delete()
    return Response({'message':"Job is deleted"},status=status.HTTP_200_OK)


@api_view(['GET'])

def getTopicStats(request,topic):
    args={'title__icontains':topic}
    jobs=Job.objects.filter(**args)

    if len(jobs) == 0:
        return Response({'message':'No stats found for {topic}'.format(topic=topic)})

    stats=jobs.aggregate(
        total_jobs=Count('title'),
        avg_positions=Avg('positions'),
        avg_salary=Avg('salary'),
        max_salary=Max('salary'),
        min_salary=Min('salary')

    )
    return Response(stats)
from django.utils import timezone

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def applyToJob(request,pk):
    
    user=request.user
    job=get_object_or_404(Job,id=pk)

    if user.userprofile.resume=='':
        return Response({'error':'Please upload your resume first'},status=status.HTTP_400_BAD_REQUEST)
    
    if job.lastDate < timezone.now():
        return Response({'error':'You cannot apply to this job,Date is over'},status=status.HTTP_400_BAD_REQUEST)
    
    alreadyApplied=job.candidateapplied_set.filter(user=user).exists()

    if alreadyApplied:
        return Response({'error':'You have already applied to this job'},status=status.HTTP_400_BAD_REQUEST)
    
    jobApplied=CandidateApplied.objects.create(
        job=job, 
        user=user,
        resume=user.userprofile.resume
        )
    
    return Response({
        'applied':True,
        'job_id':jobApplied.id
    },status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserAppliedJobs(request):
    args={'user_id':request.user.id}
    jobs=CandidateApplied.objects.filter(**args)
    serializer=CandidatesAppliedSerializer(jobs,many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isApplied(request,pk):
    user=request.user
    job=get_object_or_404(Job,id=pk)
    applied=job.candidateapplied_set.filter(user=user).exists()
    return Response(applied)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserJobs(request):
    args={'user':request.user.id}

    jobs=Job.objects.filter(**args)

    serializer=JobSerializer(jobs,many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCandidatesApplied(request,pk):
    user=request.user
    job=get_object_or_404(Job,id=pk)
    if job.user != user:
        return Response({'error':'You cannot access this job'},status=status.HTTP_403_FORBIDDEN)
    
    candidates=job.candidateapplied_set.all()

    serializer=CandidatesAppliedSerializer(candidates,many=True)

    return Response(serializer.data)




