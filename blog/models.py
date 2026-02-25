from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()

    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        null = True,
        blank = True
    )

    tags=models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts"
    )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=False)

    class Meta:
        ordering=["-created_at"]

    def __str__(self):
        return self.title
