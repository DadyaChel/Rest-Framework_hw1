from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.author}-{self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # date = models.DateTimeField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, verbose_name='tweet')

    def __str__(self):
        return self.title


class Mark(models.Model):
    mark_value = models.IntegerField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, verbose_name='tweet')

    def __str__(self):
        return self.mark_value