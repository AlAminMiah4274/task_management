from django.db import models

# Create your models here.

# many to one relationship
class Task(models.Model):
	# project = models.ForeignKey("Project", on_delete = models.CASCADE, null = True, blank = True)
	# PENDING = "PENDING"
	# IN_PROGRESS = "IN_PROGRESS"
	# COMPLETED = "CCOMPLETED"
	STATUS_CHOICES = {
		("PENDING", "Pending"),
		("IN_PROGRESS", "In Progress"),
		("COMPLETED", "Completed")
	}

	project = models.ForeignKey("Project", on_delete = models.CASCADE, default = 1, related_name = "task")
	assigned_to = models.ManyToManyField("Employee", related_name = "task")
	title = models.CharField(max_length = 250)
	description = models.TextField()
	due_date = models.DateField()
	status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = "PENDING")
	is_completed = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title

	# TaskDetail --> reverse relation:
	# details


# one to one relationship 
class TaskDetail(models.Model):
	HIGH = "H"
	MEDIUM = "M"
	LOW = "L"
	PRIORITY_OPTIONS = (
		(HIGH, "HIGH"),
		(MEDIUM, "MEDIUM"),
		(LOW, "LOW")
	)
	# std_id = models.CharField(max_length = 200, primary_key = True) # to make primary key
	# assigned_to = models.CharField(max_length=250)


	task = models.OneToOneField(Task, on_delete = models.DO_NOTHING, related_name = "details")
	priority = models.CharField(max_length = 1, choices = PRIORITY_OPTIONS, default = LOW)
	notes = models.TextField(blank = True, null = True)

	def __str__(self):
		return f"Details from task {self.task.title}"



class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField(blank = True, null = True)
	start_date = models.DateField()

	def __str__(self):
		return self.name

	# task_set --> reverse relation:
	# related name: task

"""
to get all projects: p = Project.objects.all()
to get first project: p.first()
to get the id of first project: p.first().id
"""


class Employee(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)

	# task_set --> reverse relation: 
	# related name: task

	def __str__(self):
		return self.name
