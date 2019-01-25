# View

### generic View

+ TemplateView
	+ TemplateView를 사용하는 경우에는 template_name 클래스변수를 오버라이딩으로 지정해줘야함

+ ListView
	+ 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성 2가지
		1. 컨텍스트 변수로 object_list를 사용
		2. 템플릿 파일을 `모델명소문자_list.html` 형식의 이름으로 지정

+ DetailView
	+ 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성 2가지
		1. 컨텍스트 변수로 object를 사용
		2. 템플릿 파일을 `모델명소문자_detail.html` 형식의 이름으로 지정
	+ DetailView를 상속받은 경우 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 된다.
	+ 테이블에서 기본 키로 조회해서 특정 객체를 가져오는 경우에는 테이블명, 즉 모델 클래스명만 지정해주면 된다.
	+ 조회 시 사용할 기본 키 값은 URLconf에서 추출해 뷰로 넘어온 파라미터를 사용		

+ ArchiveView(ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView)기록
	+ ArchiveIndexView = 테이블로부터 객체 리스트를 가져와, 날짜 필드를 기준으로 최신 객체를 먼저 출력함
	+ YearArchiveView = 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와, 그 객체들이 속한 월을 리스트로 출력, 날짜 필드의 연도 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
	+ MonthArchiveView = 테이블로부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와, 그리스트를 출력, 날짜 필드의 연도 및 월 파라미터는 URLconf로 추출해 뷰로 넘겨줌
	+ DayArchiveView = 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와, 그 리스트를 출력, 날짜 필드의 연도, 월, 일 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
	+ TodayArchiveView = 테이블로부터 날짜 필드가 오늘인 객체 리스트를 가져와 그 리스트를 출력, 오늘 날짜 기준으로 연월일로 지정한다는 점 이외에는 DayArchiveView와 동일

+ FormView
	+ 양식을 표시하는보기. 오류시 유효성 검증 오류로 양식을 다시 표시합니다. 성공하면 새 URL로 리디렉션됩니다.
	

+ TaggedObjectList
	+ 태그 패키지 설치후 사용 (패키지모음에 사용법있음)
	+ 템플릿 랜더링 처리만하는뷰(template_name)와 TOL(TaggedObjectList)는 ListView를 상속 받는뷰(model, template_name)(모델가 테그가 주어지면 태그가 달려있는 모델의 객체리스트를 보여줌)두개 나눠서 만들기


### 속성
+ `model = 모델이름`
	+ 사용할 모델을 불러올때
+ `form_class = 폼클래스명`
	+ 사용할 폼 클래스명 불러올때 
+ `template_name = 'xxxx.html'`
	+ 사용할 템플릿 이름
+ `context_object_name = 'test'`
	+ 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정
+ `paginate_by = 2`
	+ 한페이지에 보여주는 객체 리스트의 숫자
	+ 페이징 기능이 활성화되면 객체 리스트 하단에 페이지를 이동할수 있는 버튼을 만들수 있음
+ `make_object_list = True`
	+ True면  해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨줌
	+ 템플릿 파일에서 object_list 컨텍스트 변수를 사용할수 있음
	+ 디폴트는 False
+ `date_field = 'test'`
	+ 기준이되는 날짜 필드는 test컬럼을 사용


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	