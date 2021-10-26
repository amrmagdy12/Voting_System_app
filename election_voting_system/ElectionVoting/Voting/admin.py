from django.contrib import admin
from .models import Voter , Region , Candidate , Election , Voting_on
# Register your models here.
admin.site.register(Voter)
admin.site.register(Region)
admin.site.register(Candidate)
admin.site.register(Election)
admin.site.register(Voting_on)
