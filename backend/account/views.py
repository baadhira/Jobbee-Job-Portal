from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import *

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])

def register(request):

    data=request.data

    user=SignUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password']),

            )

            return Response(
                {
                'message':'User registered'},
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                'error':'user already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    else:
        return Response(user.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def currentUser(request):
    user = UserSerilizer(request.user)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def updateUser(request):
    user=request.user

    serializer=UserSerilizer(user,many=False)

    data=request.data

    user.first_name=data['first_name']
    user.last_name=data['last_name']
    user.username=data['email']
    user.email=data['email']

    if data['password'] != '':
        user.password=make_password(data['password'])
    
    user.save()

    serializer=UserSerilizer(user,many=False)

    return Response(serializer.data)
from .validators import *

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def uploadResume(request):
    user = request.user
    resume=request.FILES['resume']
    # print(user)   
    
    if resume=='':
        return Response({"error":"Please upload your resume"},status=status.HTTP_400_BAD_REQUEST)
    
    # isValidFile=validate_file_extension(resume.name)

    # if not isValidFile:
    #     return Response({"error":"Please upload pdf value"},status=status.HTTP_400_BAD_REQUEST)
    
    serializer=UserSerilizer(user,many=False)

    user.userprofile.resume=resume
    user.userprofile.save()

    return Response(serializer.data)

