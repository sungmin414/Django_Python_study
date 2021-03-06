# admin 

## class admin

```
예)
class BookmarkAdmin(admin.ModelAdmin)
	list_display = ('title', 'url')
	
admin.site.register(Bookmark, BookmarkAdmin)
```

```
예)
# StackedInline(세로로 나열), TabularInline(테이블 모양처럼 행으로 나열) 두가지가 있음
class PhotoInline(admin.StackedInline):
```

+ admin화면에서 지정 객체를 출력
	+ list_display = ('') 
+ 테이블명 객체명에 복수형 접미사(s)를 추가하고 첫글자가 대분자로 표시된다 싫다면
	+ `verbose_name_plural` 메타 옵션으로 변경가능
+ admin 객체명이 정의한 모델클래스 이름을 소문자와 공백으로 바꿈 싫다면
	+ `verbose_name` 옵션으로 변경가능

+ 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
	+ list_filter = ('')
+ 검색 박스를 표시하고 검색할 객체 설정
	+ search_fields = ('')
+ xxx 필드는 xxx필드를 사용해 미리 채워지도록 함
	+ prepopulated_fields = {'slug': ('title',)}
+ 이미 입력된 객체 외에 추가로 입력할수 있는 테이블 객체의 수 2개
	+ extra = 2
+ 클래스에서 정의한 사항을 같이 보기
	+ inlines = [클레스명]
      