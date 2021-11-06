from django.db.models import query
from django.http.request import QueryDict
from django.shortcuts import render
from django.views import generic
from rest_framework.decorators import api_view, permission_classes , action
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics , mixins ,viewsets 
from .models import *
from .serializers import * 
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.response import Response 
from django.contrib.auth import logout

# Create your views here.

@api_view(['POST'])
def logout_vw(request) :
    request.user.auth_token.delete()
    return Response({"auth" : "Logout done succesfully "} , status = status.HTTP_200_OK)

#Admin users (Superusers)
class handle_voter(viewsets.ModelViewSet) :
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [IsAdminUser]
#Admin users (Superusers)
class handle_candidate(viewsets.ModelViewSet) :
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAdminUser]
#Admin users (Superusers)
class handle_election(viewsets.ModelViewSet) :
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [IsAdminUser]
#Admin users (Superusers)
class handle_voting_on (viewsets.ModelViewSet) :
    queryset = Voting_on.objects.all()
    serializer_class = VotingonSerializer
    permission_classes= [IsAdminUser]

class addlist_elections (generics.ListCreateAPIView) :
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAdminUser]

#public users 
class list_Candidates(viewsets.ReadOnlyModelViewSet) : #first view for listing candidates 
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes= [IsAuthenticated]
    
class list_Election(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def list(self , request) :
        query = Election.objects.all()
        serializer = ElectionSerializer(query , many=True)
        return Response(serializer.data)
@api_view(['POST'])        
def vote_on (request) :
         if request.method == 'POST' :
           try :
               if(request.user.personal_id == request.data['voter']):
                    Voting_on.objects.get(voter = request.user.personal_id , candidate = request.data['candidate'] , election = request.data['election'])
               else :
                   return Response({"Input error" : "Conflict user can't vote"})
           except Voting_on.DoesNotExist :
                serializer = VotingonSerializer(data = request.data)
                if serializer.is_valid() :
                        serializer.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                else :
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
           else :
                 return Response({"error" : "this user already voted"} , status=status.HTTP_403_FORBIDDEN)      
        
@api_view(['PUT'])        
def change_vote(request , cand_id , elec_id):
           query = QueryDict 
           if request.method == 'PUT' :
            try :
               if(request.user.personal_id == request.data['voter']):
                   query =  Voting_on.objects.get(voter = request.user.personal_id , candidate = request.data['candidate'] , election = request.data['election'])
               else :
                   return Response({"[Change_vote] Input error" : "Conflict user can't vote"})
            except Voting_on.DoesNotExist :
                serializer = VotingonSerializer(query , data = request.data)
                if serializer.is_valid() :
                        serializer.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                else :
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
           else :
                 return Response({"error" : "this user already voted"} , status=status.HTTP_403_FORBIDDEN)
                