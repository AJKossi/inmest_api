from django.contrib import admin

from main.models import ClassAttendance, ClassSchedule, Course, Query, QueryComment

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=("course_name","date_created","date_modified")
admin.site.register(Course,CourseAdmin)

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date_and_time', 'end_date_and_time', 'is_repeated', 'repeat_frequency', 'is_active', 'organizer', 'cohort', 'venue')
    list_filter = ('is_active', 'is_repeated', 'cohort')
    search_fields = ('title', 'description')
admin.site.register(ClassSchedule,ClassScheduleAdmin)


class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'submitted_by', 'assigned_to', 'resolution_status', 'date_created', 'date_modified', 'author')
    list_filter = ('resolution_status', 'date_created', 'date_modified')
    search_fields = ('title', 'description')
admin.site.register(Query,QueryAdmin)


class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ('query', 'comment', 'date_created', 'date_modified', 'author')
    list_filter = ('date_created', 'date_modified')
    search_fields = ('query__title', 'comment')
admin.site.register(QueryComment,QueryCommentAdmin)


class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ('class_schedule', 'attendee', 'is_present', 'date_created', 'date_modified', 'author')
    list_filter = ('is_present', 'date_created', 'date_modified')
    search_fields = ('class_schedule__title', 'attendee__first_name', 'attendee__last_name')
admin.site.register(ClassAttendance,ClassAttendanceAdmin)