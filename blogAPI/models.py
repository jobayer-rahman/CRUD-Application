from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        DeletedAuthor.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
            email=self.email
        )
        super().delete(*args, **kwargs)

class DeletedAuthor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    deletion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        DeletePost.objects.create(
            author=self.author,
            title=self.title,
            slug=self.slug,
            body=self.body
        )
        super().delete(*args, **kwargs)

class DeletePost(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True, blank=True)
    body = models.TextField()
    deletion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def delete(self, *args, **kwargs):
        DeleteComment.objects.create(
            post=self.post,
            author=self.author,
            body=self.body
        )
        super().delete(*args, **kwargs)

class DeleteComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    deletion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
