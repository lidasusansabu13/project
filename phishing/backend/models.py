# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


WEBSITE_SAFE = 1
WEBSITE_UNSAFE = -1
WEBSITE_NEUTRAL = 0

STATUS_CHOICES = (
    (WEBSITE_SAFE, 'SAFE'),
    (WEBSITE_NEUTRAL, 'NEUTRAL'),
    (WEBSITE_UNSAFE, 'UNSAFE')
)

class Website(models.Model):
    """

    """

    url = models.TextField()
    time = models.DateField(default=timezone.now())
    status = models.IntegerField( default=WEBSITE_NEUTRAL,
        choices=STATUS_CHOICES)

    def __unicode__(self):
        """Object name in django admin."""
        return self.url


class Feature_score(models.Model):
    """

    """

    website = models.ForeignKey(Website)
    feature_name = models.CharField(max_length=200)
    position = models.IntegerField()
    score = models.IntegerField( default=WEBSITE_NEUTRAL,
        choices=STATUS_CHOICES)
    time = models.DateField(default=timezone.now())

    def __unicode__(self):
        """Object name in django admin."""
        return self.feature_name + "  :  " + self.website.url
