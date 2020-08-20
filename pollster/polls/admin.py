from django.contrib import admin

# import models
from .models import Question, Choice

# site titles
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Pollster Admin"

# Sets the choices to be inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Displays choices inside of questions 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# Registers our model
admin.site.register(Question, QuestionAdmin)