# settings.py 설정

## 디렉토리 추가 

### TEMPLATES
+ DIRS 항목은 프로젝트 템플릿 파일이 위치한 디렉터리를 지정, 템플릿 파일을 찾을 때, 프로젝트 템플릿 디렉터리는 애플리케이션 템플릿 디렉터리보다 먼저검색
	+ `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') -> TEMPLATES안에 DIRS에 TEMPLATES_DIR 넣기`

### STATICFILES
+ STATICFILES_DIRS 항목은 프로젝트 정적 파일이 위치한 디렉터리를 의미하는데 수동으로 지정
+ 템플릿 파일을 찾는 순서와 비슷하게 정적 파일을 찾을 때도 각 애플리케이션 static/ 디렉터리보다 STATICFILES_DIRS항목으로 지정한 디렉터리를 먼저 검색
	+ `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`

### MEDIA
+ `MEDIA_URL = '/media/'`
+ `MEDIA_ROOT = os.path.join(BASE_DIR, 'media') `

### 시간, 언어 설정
+ `LANGUAGE_CODE = 'ko-kr'`
+ `TIME_ZONE = 'Asia/Seoul'`

### 앱등록
+ 애플리케이션 설정 클래스
	+ 애플리케이션의 설정 클래스는 해당 애플리케이션에 대한 메타 정보를 저장하기 위한 클래스로, django.apps.AppConfig클래스를 상속받아 작성
	+ 앱 설정 클래스에는 앱 이름(name) 레이블( label) 별칭( verbose_name) 경로(path) 등을 설정 할수 있으며 이름(name)은 필수 속성
	+ 