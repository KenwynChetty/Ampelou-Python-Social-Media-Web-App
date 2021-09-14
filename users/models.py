from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOICES = [
    ('M', 'Married'),
    ('S', 'Single'),
    ('R', 'In A Relationship'),
]

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=255, blank=True) 
    location = models.CharField(max_length=30, blank=True)
    relationship = models.CharField(max_length=20,choices=CHOICES, default='S')
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(max_length=6, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

        #def save(self, force_insert=False, force_update=False, using=None,
        #update_fields=None):
        #super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Follow(models.Model):
    user = models.ForeignKey(User,
                             related_name='user',
                             on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User,
                                    related_name='follow_user',
                                    on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
