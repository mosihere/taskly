from django.db import models



class Task(models.Model):
    BACKLOG_STATUS = 'B'
    IN_PROGRESS_STATUS = 'I'
    DONE_STATUS = 'D'

    TASK_STATUSES_CHOICES = (
        (BACKLOG_STATUS, 'Backlog'),
        (IN_PROGRESS_STATUS, 'In Progress'),
        (DONE_STATUS, 'Done')
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=TASK_STATUSES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title