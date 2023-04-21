from django.db import models


class UniversityCampus(models.Model):
    """this is the information that the user can input in the fields"""
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        """this will display the name of the campus and the state from the user creation from the fields above"""
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"


