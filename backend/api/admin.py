from django.contrib import admin

# Register your models here.

from .models import Question
admin.site.register(Question)

from .models import User
admin.site.register(User)

from .models import Subject
admin.site.register(Subject)

from .models import Project
admin.site.register(Project)

from .models import Comment
admin.site.register(Comment)