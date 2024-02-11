from django.contrib import admin

from users.models import IMUser,Cohort,CohortMember

# Register your models here.
# Register IMUser model.
class IMUserAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","is_active","user_type","date_created")
admin.site.register(IMUser,IMUserAdmin)

# Register Cohort model.
class CohortAdmin(admin.ModelAdmin):
    list_display=("name","description","year","start_date","end_date","is_active","date_created","date_modified","author")
admin.site.register(Cohort,CohortAdmin)

class CohortMemberAdmin(admin.ModelAdmin):
    list_display=("cohort","member","is_active","date_created","date_modified","author")
admin.site.register(CohortMember,CohortMemberAdmin)