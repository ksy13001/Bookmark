from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')   # 어드민 페이지에서 'Site URL' 이라고 표시

    def __str__(self):
        return self.site_name + ' : ' + self.url

    # 업데이트시 detail 화면으로 돌아가기
    def get_absolute_url(self):
        # reverse -> url 패턴과 추가 인자를 받아서 url을 생성
        return reverse('detail', args=[str(self.id)])