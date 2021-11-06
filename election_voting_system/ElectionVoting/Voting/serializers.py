#Voter serlializer
from rest_framework import serializers
from .models import *

class VoterSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Voter 
        fields = ['personal_id' , 'votekey' , 'region']


class CandidateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Candidate 
        fields = ['id','name' , 'symbol' , 'description' , 'election']

class ElectionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Election 
        fields = ['election_name' ,'region']
class RegionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Region 
        fields = ['__all__']

class VotingonSerializer(serializers.ModelSerializer):
    class Meta :
        model = Voting_on 
        fields = ['voter' , 'candidate' ,'election']
