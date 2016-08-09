from django.contrib import admin
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
