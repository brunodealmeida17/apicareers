from django.db import models


class Career(models.Model):    
    username = models.CharField(max_length=50)
    create_datetime = models.DateTimeField(auto_now_add=True)   
    title = models.CharField(max_length=100)
    content = models.TextField()
    

    class Meta:
        verbose_name = 'career'
        verbose_name_plural = 'careers'
        ordering = ['id']

    def __str__(self):
        return self.title
