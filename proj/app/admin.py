from django.contrib import admin
from app.models import Profile, Question, Answer
 
class ProfileAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['description', 'created']
    # fields to filter the change list with
    list_filter = ['active', 'created']
    # fields to search in change list
    search_fields = ['description', 'interests']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
 
 
admin.site.register(Profile, ProfileAdmin)

class QuestionAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['body', 'username']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['body']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("body",)}    
 
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['body', 'username']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['body']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True   
 
admin.site.register(Answer, AnswerAdmin)
