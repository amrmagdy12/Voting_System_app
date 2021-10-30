from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics , mixins 
from .models import *
from .serializers import * 
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.


class add_list_Voter(generics.ListCreateAPIView) :
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

class list_Candidates(generics.ListAPIView) :
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class add_Candidate(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # permission_classes = [IsAuthenticated]

