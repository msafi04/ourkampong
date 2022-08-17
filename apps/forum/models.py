from django.db import models

from apps.member.models import Member

class Post(models.Model):
    title = models.CharField(max_length = 255)
    intro = models.TextField(blank = True, null = True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    member = models.ForeignKey(Member, related_name = 'posts', on_delete = models.CASCADE)

    post_likes = models.ManyToManyField(Member, related_name = 'like_post', default = None, blank = True)

    class Meta:
        ordering = ['-date_added']

    def total_post_likes(self):
        return self.post_likes.count()

    def comment_count(self):
        return self.comment_set.all().count() #Django backward relations
    
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField(default = None)
    comment_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.content