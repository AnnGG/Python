from django.contrib import admin
from .models import Askstor, Newstor, Showstor, Jobstor

admin.site.register(Askstor)
admin.site.register(Newstor)
admin.site.register(Jobstor)
admin.site.register(Showstor)

