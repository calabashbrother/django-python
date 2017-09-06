#! /usr/bin/env python3
# __*__ encoding: utf-8 __*__

'''
schema

'''
from django.db import models

class User(models.Model):
    """docstring for user"""
    # id = models.CharField(max_length=32)
    user_id = models.CharField(max_length=12)
    user_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name
