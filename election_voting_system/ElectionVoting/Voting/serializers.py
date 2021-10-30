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
        fields = ['__all__']

class ElectionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Election 
        fields = ['__all__']
class RegionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Region 
        fields = ['__all__']

class VotingonSerializer(serializers.ModelSerializer):
    class Meta :
        model = Voting_on 
        fields = ['__all__']
