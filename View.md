# View

### generic View

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

+ ArchiveView(ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView)
	+ ArchiveIndexView = 테이블로부터 객체 리스트를 가져와, 날짜 필드를 기준으로 최신 객체를 먼저 출력함
	+ YearArchiveView = 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와, 그 객체들이 속한 월을 리스트로 출력, 날짜 필드의 연도 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
	+ MonthArchiveView = 테이블로부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와, 그리스트를 출력, 날짜 필드의 연도 및 월 파라미터는 URLconf로 추출해 뷰로 넘겨줌
	+ DayArchiveView = 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와, 그 리스트를 출력, 날짜 필드의 연도, 월, 일 파라미터는 URLconf에서 추출해 뷰로 넘겨줌
	+ TodayArchiveView = 테이블로부터 날짜 필드가 오늘인 객체 리스트를 가져와 그 리스트를 출력, 오늘 날짜 기준으로 연월일로 지정한다는 점 이외에는 DayArchiveView와 동일
