from uuid import uuid4

from django.db import models
from zeep.client import Client

# Create your models here.
url = "http://it.bmc.uu.se/andlov/php/uup-soap/example/demo/calculator.php?WSDL"

client = Client(url)


class TaskModel(models.Model):
    """ Model for tasks
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=32)
    description = models.TextField()
    owner = models.CharField(max_length=32)
    estimated_time = models.PositiveIntegerField(default=0)
    time_worked = models.FloatField(default=0)
    time_left = models.FloatField(default=0)
    overtime_worked = models.FloatField(default=0)

    @property
    def time_calculator(self):
        """ Use web service (SOAP) to perform time calculations
            and update the corresponding tasks in the DB
        """
        if self.time_worked > 0:
            time = client.service.substract(
                self.estimated_time, self.time_worked)
        if time <= self.estimated_time and time > 0:
            return time, self.overtime_worked
        elif time < 0:
            return 0, client.service.multiply(time, -1)

    def save(self):
        self.time_left, self.overtime_worked = self.time_calculator
        super(TaskModel, self).save()
