from django.contrib import admin

from .models import Patent, PatentAuthor, PatentCode, LawStatusEvent, InterPatentCode
# Register your models here.

admin.site.register(Patent)

admin.site.register(PatentAuthor)

admin.site.register(LawStatusEvent)

admin.site.register(InterPatentCode)

admin.site.register(PatentCode)