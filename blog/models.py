from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    # 업로드할 폴더 지정 
    # settings.py에 MEDIA_URL로 지정해둔 media 폴더 안에 blog 폴더를 만들어 관리하겠다. 
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]