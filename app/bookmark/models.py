from django.db import models


class Bookmark(models.Model):
    # blank, null 공백값을 가질수 있고 값이 없을수도 있다
    title = models.CharField(max_length=100, blank=True, null=True)
    # url 컬럼에 대한 레이블 문구(필드별칭이라고도함),
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title