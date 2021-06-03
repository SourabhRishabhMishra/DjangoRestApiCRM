from django.contrib import admin

from .models import Account, Activity, ActivityStatus, Contact, ContactSource, ContactStatus
# Register your models here.

admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(ActivityStatus)
admin.site.register(Contact)
admin.site.register(ContactSource)
admin.site.register(ContactStatus)