# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


'''models are the database layout plus some metadata. A model is a definitive
source of truth for the database; the datamodel should be defined in one place
and then information should be automatically retrieved from it'''

''' the models are subclasses in django.db.models.Model '''

''' each field is defined by a field class; Charfields are for character fields
DateTimeFields are DateTimeFields'''
