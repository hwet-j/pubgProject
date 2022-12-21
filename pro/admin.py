from django.contrib import admin
from .models import PgcList, MatchData, Video

# Register your models here.


admin.site.register(PgcList)
admin.site.register(MatchData)
admin.site.register(Video)