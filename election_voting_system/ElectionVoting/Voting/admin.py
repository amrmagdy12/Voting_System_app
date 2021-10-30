from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = VoterCreationForm
    form = VoterChangeForm
    model = Voter
    list_display = ('personal_id', 'votekey' , 'region' ,'is_staff', 'is_active',)
    list_filter = ('personal_id', 'votekey', 'region')
    fieldsets = (
        (None, {'fields': ('personal_id', 'votekey', 'region')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('personal_id', 'votekey','region', 'is_staff', 'is_active',)}
        ),
    )
    #search_fields = ('email',)
    ordering = ('personal_id',)


admin.site.register(Voter , CustomUserAdmin)
admin.site.register(Candidate)
admin.site.register(Voting_on)
admin.site.register(Election)
admin.site.register(Region)
