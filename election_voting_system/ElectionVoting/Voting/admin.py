from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Voting_on)
admin.site.register(Election)
admin.site.register(Region)
