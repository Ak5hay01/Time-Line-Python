from django.db import models
import datetime
import pytz


# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    # Dynmically finding the location and showing datetime
    #     LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    #     your_now = self.created.astimezone(LOCAL_TIMEZONE)
    #
    #     date_str = your_now.strftime("%d %b %Y - %I:%M %p")
    #     return f" {self.title} - {date_str}"

    # Hard coded location
        tz = pytz.timezone('Asia/Kolkata')
        your_now = self.created.astimezone(tz)

        date_str = your_now.strftime("%d %b %Y - %I:%M %p")
        return f" {self.title} - {date_str}"

