# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Elderly(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
	caregiver_mail = models.TextField()
	
	class Meta:
		db_table = 'Elderly'

class Elderlyxcondition(models.Model):
	surrogate_key = models.IntegerField(db_column='ignorable', primary_key=True, default=-1)
	elderly_id = models.IntegerField(db_column='elderly_ID')  # Field name made lowercase.
	condition_id = models.IntegerField(db_column='condition_ID')  # Field name made lowercase.
	
	class Meta:
		db_table = 'ElderlyXCondition'
		unique_together = (('elderly_id', 'condition_id'))

class Elderlyxinterest(models.Model):
	surrogate_key = models.AutoField(db_column='ignore', primary_key=True, default=-1)
	elderly_id = models.IntegerField(db_column='elderly_ID')  # Field name made lowercase.
	interest_id = models.IntegerField(db_column='interest_ID')  # Field name made lowercase.
	
	class Meta:
		db_table = 'ElderlyXInterest'
		unique_together = (('elderly_id', 'interest_id'))

class Friend(models.Model):
	surrogate_key = models.AutoField(db_column='ignore', primary_key=True, default=-1)
	friend1 = models.IntegerField(db_column='Friend1')  # Field name made lowercase.
	friend2 = models.IntegerField(db_column='Friend2')
	
	class Meta:
		db_table = 'Friend'
		unique_together = (('friend1', 'friend2'))

class Interest(models.Model):
	interest_id = models.AutoField(db_column='interest_ID', primary_key=True, default=-1)  # Field name made lowercase.
	interest_name = models.TextField()
	
	class Meta:
		db_table = 'Interest'

class MedicalCondition(models.Model):
	condition_id = models.AutoField(db_column='condition_ID', primary_key=True, default=-1)  # Field name made lowercase.
	condition_name = models.TextField()
	
	class Meta:
		db_table = 'Medical_Condition'

class Request(models.Model):
	request_id = models.AutoField(db_column='request_ID', primary_key=True)  # Field name made lowercase.
	content = models.TextField()
	time = models.TextField()
	category = models.TextField()
	requester = models.IntegerField()
	volunteer = models.IntegerField(blank=True, null=True)
	
	class Meta:
		db_table = 'Request'

class User(models.Model):
	username = models.TextField()
	id = models.AutoField(db_column='ID', primary_key=True, default=-1)  # Field name made lowercase.
	location = models.TextField()
	bio = models.TextField()
	photograph = models.ImageField(upload_to='user_dp/')
	age = models.IntegerField()
	mail = models.TextField()
	
	class Meta:
		db_table = 'User'

class Volunteer(models.Model):
	id = models.AutoField(db_column='ID', primary_key=True, default=-1)  # Field name made lowercase.
	rating = models.IntegerField()  # This field type is a guess.
	score = models.IntegerField()
	occupation = models.TextField()
	
	class Meta:
		db_table = 'Volunteer'

class VolunteerReview(models.Model):
	surrogate_key = models.AutoField(db_column='ignore', primary_key=True, default=-1)
	volunteer_id = models.IntegerField(db_column='volunteer_ID')  # Field name made lowercase.
	elderly_id = models.IntegerField(db_column='elderly_ID')  # Field name made lowercase.
	review_contents = models.TextField(blank=True, null=True)
	star_rating = models.IntegerField()
	
	class Meta:
		db_table = 'Volunteer_Review'
		unique_together = (('volunteer_id','elderly_id'))
