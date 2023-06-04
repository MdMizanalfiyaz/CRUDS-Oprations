from django.db import models


class Profile(models.Model):
    RELIGION = (
        ("Islam", "Islam"),
        ("Hindu", "Hindu"),
        ("Christan", "Christan"),
        ("Buddhism", "Buddhism"),

    )

    Gender = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),

    )

    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pic/', default='default/default.jpg.png', blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    phone_no = models.TextField(max_length=15, blank=True, null=True)
    date_of_birth = models.TextField(max_length=12, blank=True, null=True)
    religion = models.CharField(max_length=10, choices=RELIGION, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=Gender, blank=True, null=True)

    def __str__(self):
        return str(self.name)
