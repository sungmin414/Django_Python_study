# model

### class 필드 속성
+ `CharField('TITLE', max_length=255)`
	+ 숫자와 문자를 같이 입력가능한 필드
	+ TITLE은 컬럼에대한 레이블, 레이블은 폼화면에 나타내는 문구
+ `SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')`
	+ slug 컬럼은 제목의 별칭
	+ unique는 특정 포스트를 검색 시 기본 키 대신에 사용
	+ allow_unicode는 한글 처리가능하게 해줌
	+ help_text는 해당 컬럼을 설명해주는 문구로 폼화면에 나타냄
+ `TextField('CONTENT')`
	+ 여러줄을 입력가능한 필드
+ `DateTimeField('Create Date', auto_now_add=True, auto_now=True)`
	+ 시간을 나타내는 필드
	+ auto_now_add는 객체가 생성될 때의 시각을 자동으로 기록
	+ auto_now는 객체가 데이터베이스에 저장될 때의 시각을 자동으로 기록(객체가 변경 될 때의 시각이 기록)



### class Meta 속성
+ verbose_name = ''
	+	테이블의 별칭을 단수와 복수로 가질수 있음, 사용자가 읽기 쉬운 모델 객체의 이름 관리
+ verbose_name_plural = ''
	+	테이블의 복수 별칭 변경
+ db_table = ''
	+	데이터베이스 이름변경
+ ordering = ('-')
	+	모델 객체리스트 내림차순 정렬

	
```
# 메소드가 정의된 객체를 지칭하는  URL을 반환, 메소드 내에서는 장고의 내장함수인
	reverse()함수를 호출
def get_absolute_url(self):
	return reverse('blog:post_detail', args=(self.slug,))

# modify_date 컬럼을 기준으로 이전 포스트를 반환, 메소드 내에서는 장고의
	내장함수인 get_previous_by_mpdeify_date()를 호출
def get_previous_post(self):
    return self.get_previous_by_modify_date()

# modify_date 컬럼을 기준으로 다음 포스트를 반환, 메소드 내에서는 장고의
	내장함수인 get_next_by_mpdeify_date()를 호출
def get_next_post(self):
    return self.get_next_by_modify_date()	
```