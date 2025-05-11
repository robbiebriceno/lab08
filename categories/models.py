from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Then add to quizzes/models.py:
# category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, related_name='quizzes')
# tags = models.ManyToManyField('categories.Tag', related_name='quizzes', blank=True)
