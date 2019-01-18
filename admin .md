# admin 

## class admin

```
예)
class	BookmarkAdmin(admin.ModelAdmin)
	list_display = ('title', 'url')
	
admin.site.register(Bookmark, BookmarkAdmin)
```

+ admin화면에서 지정 객체를 출력
	+ list_display = ('') 
+ 테이블명 객체명에 복수형 접미사(s)를 추가하고 첫글자가 대분자로 표시된다 싫다면
	+ `verbose_name_plural` 메타 옵션으로 변경가능
+ admin 객체명이 정의한 모델클래스 이름을 소문자와 공백으로 바꿈 싫다면
	+ `verbose_name` 옵션으로 변경가능

	