from __future__ import unicode_literals
from django.db import models
import bcrypt
from django.shortcuts import render, HttpResponse, redirect
import sys, re

rejectEmail = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def verify(self, postData):
        errors = {}
        if len(postData['password']) < 3:
            errors["password"] = "Password should be more than 3 characters"
        if len(postData['email']) < 5 or not rejectEmail.match(postData['email']):
            errors['email'] = "Email cannot be empty!"
        if len(postData['password']) < 1:
            errors['password'] = "Password cannot be empty"
        return errors

    def creater(self, postData):
        errors = {}
        if len(postData['cPassword']) < 3:
            errors["cPassword"] = "Password should be more than 3 characters"

        if len(postData['conPassword']) < 3:
            errors["conPassword"] = "Password should be more than 3 characters"

        if len(postData['eEmail']) < 5:
            errors['eEmail'] = "Email cannot be empty!"

        if not rejectEmail.match(postData['eEmail']):
            errors['eEmail'] = "Email is invalid!"

        if postData['cPassword'] != postData['conPassword']:
            errors['cPassword'] = "Passwords do not match!"

        if postData['nName'] < 2:
            errors['nName'] = "Full name must be longer than 2 characters."

        if postData['DOB'] < 18:
            errors['DOB'] = "You must be 18 to enter.. But it's not like i'm gonna stop you from doing so."
        return errors

    def addQuote(self, postData):
        errors = {}
        if len(postData['quote']) < 10:
            errors["quote"] = "Item name should be more than 10 characters"

        if len(postData['quotedBy']) < 3:
            errors["quotedBy"] = "Quote Author should be more than 3 characters"

        if len(postData['addBy']) < 2:
            errors["addBy"] = "Name should be more than 2 characters"
        return errors


##################################################################################################################
class Quotes(models.Model):
    quotedBy = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    addBy = models.CharField(max_length=255)
    # userFav = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


##################################################################################################################)
class FaveQuotes(models.Model):
    quote = models.CharField(max_length=255)
    quoteBy = models.CharField(max_length=255)
    # usersFave = models.ForeignKey(Users, related_name="users")
    add_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


##################################################################################################################
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    # FavQuote = models.ForeignKey(FaveQuotes, related_name='favQuotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
