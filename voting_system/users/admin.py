from django.contrib import admin
from .models import VotingUser
# Register your models here.
@admin.register(VotingUser)
class VotingUserAdmin(admin.ModelAdmin):
    list_display = ['name','qr_code','vote_first_king','vote_first_queen','vote_king','vote_queen']


    
