from django.contrib import admin
from .models import Question, Choice


# Register your models here.



class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0
    readonly_fields = ['votes']



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text', 'pub_date']




@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['votes']
    search_fields = ['choice_text', 'question__question_text']
    list_display = ['get_question_text', 'choice_text', 'votes']

    @admin.display(description='Question text')
    def get_question_text(self, obj):
        return obj.question.question_text

