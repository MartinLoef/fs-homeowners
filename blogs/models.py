from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    blog_image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return "BlogID: {0} / User: {1} / Date: {2} / Title: {3}".format(
            self.id, self.author, self.published_date, self.title)

class BlogComment(models.Model):
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment_blog")
    authorid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    blog_comment = models.CharField(max_length=125)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "BlogCommentID: {0} / User: {1} / Date: {2}".format(
            self.id, self.authorid, self.created_date)

class BlogLike(models.Model):
    BlogLikeId = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_like")
    BlogLikedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_liked_by_user")
    
    def __int__(self):
        return "BlogLikeId: {0} / BlogID: {1} / User: {2}".format(
            self.id, self.BlogLikeId, self.user)