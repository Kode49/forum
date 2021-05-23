from django.db import models

# Create your models here.

class Question(models.Model): 
    id = models.IntegerField(primary_key=True)
    themaId = models.IntegerField()
    userId = models.IntegerField()

class User(models.Model): 
        Firstname = models.TextField()
        Surname = models.TextField()
        id = models.IntegerField(primary_key=True)
        Question = models.TextField(foreign_key=True)
        Comment = models.TextField(foreign_key=True)
        password = models.IntegerField()
        Mark = models.IntegerField()

 class Subject(models.Model):
     id = models.IntegerField(primary_key=True)
     Subject = models.TextField()
     ProjectId = models.IntegerField(foreign_key=True)

class Member(models.Model):
     id = models.IntegerField(primary_key=True)
     Name = models.TextField()
     QuestionId = models.IntegerField(foreign_key=True)

class Project(models.Model):
     id = models.IntegerField(primary_key=True)
     Projectname = models.TextField()
     NumberofMembers = models.IntegerField()

class Comment(models.Model):
     id = models.IntegerField(primary_key=True)
     UserId = models.IntegerField(foreign_key=True)
     Comment = models.TextField()
     Modified = models.TextField()
     