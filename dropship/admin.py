from django.contrib import admin

from .models import Label, Member, Sprint, User, Project, Issue,Comment

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Member)
admin.site.register(Label)
admin.site.register(Sprint)
admin.site.register(Comment)


