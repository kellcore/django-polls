import datetime

from django.db import models
from django.utils import timezone


# models -> essentially your database layout with additional metadata
# a model is the single, definitive source of info about your data
# contains essential fields/behaviors of the data you're storing
# django follows the DRY principle -> Don't Repeat Yourself
# goal is to define your data model in one place and automatically derive things from it

# three step guide to updating models:
# change your models in models.py
# run python manage.py makemigrations to create migrations for those changes (run python manage.py sqlmigrate appname numberofmigration to have the SQL print to your screen for review before updating it)
# run python manage.py migrate to apply those changes to the database

# create two Models: Question and Class
# Question has a question and a publication date
# Choice has two fields: the text of the choice and a vote tally
# each Choice is associated with a Question

# each model is represented by a class that subclasses django.db.models.Model
# each model has a number of class variables, each of which represents a database field in the model
class Question(models.Model):
    # each field is represented by an instance of a Field class -> this tells Django which type of data each field holds
    # your database will use the name of each field instance as the column name
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # a relationship is defined using ForeignKey
    # this tells Django each Choice is related to a single Question
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
