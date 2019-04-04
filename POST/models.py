from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Article(models.Model):
    TYPE = (('TEXT', '文字'), ('PIC', '图片'))
    title = models.CharField("文章标题", max_length=60)
    summary = models.CharField("文章摘要", max_length=400)
    body = models.FileField(upload_to='HTML/%Y/%m/%d')
    publish_time = models.DateTimeField("发布时间", default=timezone.now)
    tags = TaggableManager("文章标签")
    cover = models.TextField(
        "封面图片", default="http://p2p0dadp7.bkt.clouddn.com/Nighthawks.jpg")
    type = models.CharField("展示类型", max_length=20,
                            choices=TYPE, default='TEXT')

    def __str__(self):
        return self.title

    def is_message(self):
        return False


class Message(models.Model):
    body = models.TextField("消息内容")
    publish_time = models.DateTimeField("发布时间", default=timezone.now)

    def __str__(self):
        return self.body

    def is_message(self):
        return True
