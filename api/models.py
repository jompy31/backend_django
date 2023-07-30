from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_status = models.CharField(
        max_length=20,
        choices=(
            ('customer', 'Customer'),
            ('user', 'User'),
            ('administrator', 'Administrator'),
        ),
        default='customer'
    )
    company = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=(
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        )
    )
    status = models.CharField(
        max_length=10,
        choices=(
            ('new', 'New'),
            ('contacted', 'Contacted'),
            ('winner', 'Winner'),
        ),
        default='new'
    )
    number = models.CharField(max_length=20, blank=True, null=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='lead_comments')

    def __str__(self):
        return self.name


class Comment(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_comments')
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} for Lead {self.lead.name}"


