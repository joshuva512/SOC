from django.db import models


class COMPUTER_HARDWARE_SERVICING_AND_NETWORKING(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to="s1")
    def __str__(self):
        return self.name


class MICROCONTROLLER_AND_ANDROID_OS(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to="s2")
    def __str__(self):
        return self.name


class VLSI(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to="s3")
    def __str__(self):
        return self.name


class DIGITAL_COMMUNICATION(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to="s4")
    def __str__(self):
        return self.name
