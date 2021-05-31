from django.db import models


class User(models.Model):
    Firstname = models.TextField()
    Surname = models.TextField()
    bild = models.CharField
    id = models.IntegerField(primary_key=True)
    password = models.IntegerField()
    Mark = models.IntegerField()


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    Subject = models.TextField()


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    Projectname = models.TextField()
    description = models.TextField()
    NumberofMembers = models.IntegerField()


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Comment = models.TextField()
    Modified = models.BooleanField
