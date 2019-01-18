from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    # 화면에 보여줄 객체 설정
    list_display = ('title', 'modify_date')
    # 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    list_filter = ('modify_date',)
    # 검색박스를 표시하고 검색할 객체 설정
    search_fields = ('title', 'content')
    # slug 필드는 title 필드를 사용해 미리 채워지도록 함
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
