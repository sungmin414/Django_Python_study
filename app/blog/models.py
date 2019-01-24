from django.db import models
# reverse() 함수는 URL 패턴을 만들어주는 장고의 내장 함수
from django.urls import reverse
from tagging.fields import TagField


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    # SlugField 에 unique 옵션을 추가해 특정 포스트를 검색 시 기본 키대신에 사용, allow_unicode 옵션을 추가하면 한글 처리가능
    # help_text 는 해당 컬럼을 설명해주는 문구로 폼 화면에 나타냄
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    content = models.TextField('CONTENT')
    # auto_now_add 객체가 생성될 떄의 시각을 자동으로 기록
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # auto_now 객체가 변결 될때의 시각이 기록
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    # 태그 기능 필드
    tag = TagField()

    class Meta:
        # 사용자가 읽기 쉬운 모델 객체의 이름관리
        verbose_name = 'post'
        # 위와 비슷함
        verbose_name_plural = 'posts'
        # 데이터베이스 이름설정
        db_table = 'my_post'
        # 리스트 내림차순
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    # 메소드가 정의된 객체를 지칭하는 URL을 반환, 메소드 내에서는 장고의 내장함수인 reverse()함수호출
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_date 컬럼기준으로 이전 포스트 반환
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # modify_date 컬럼기준으로 다음 포스트 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()



