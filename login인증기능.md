## login 

+ login.html
	+ AuthenticationForm 장고에서 제공해주는 로그인용 기본 폼
+ `password_change_form.html`
	+ PasswordChangeForm 장고에서 제공해주는 기본 폼

```
templates에서 form (username, password) 가져오기
{{ form.username_label_tag }} {{ form.username }}
{{ form.password_label_tag }} {{ form.password }}
결과값
username:
password:

비밀번호 change시 사용 
{{ form.old_password.label_tag }} {{ form.old_password }}
{{ form.new_password1.label_tag }} {{ form.new_password1 }}
{{ form.new_password2.label_tag }} {{ form.new_password2 }}

```

### templates

```
{% extends 'base.html' %}

{% block title %}login.html{% endblock %}

{% load staticfiles %}
{% block extrastyle %}{% static 'css/forms.css' %}{% endblock %}

{% block content %}
<div id="content">
    <h1>Please Login</h1>

    <form action="." method="POST">
        {% csrf_token %}
# 폼 내용에 에러가 있는경우 에러메세지 출력      
        {% if form.errors %}
        <p class="errornote">Wrong! Please correct the error(s) below.</p>
        {% endif %}

        <p>Please enter your id and password.</p>
# fieldset 폼에서 비슷한 요소들을 묶어주는 역활 
        <fieldset class="aligned">
            <div class="form-row">
                {{ form.username.label_tag }} {{ form.username }}
            </div>

            <div class="form-row">
                {{ form.password.label_tag }} {{ form.password }}
            </div>
        </fieldset>

        <div class="submit-row">
            <input type="submit" value="Log In">
# 폼을 제출 시 폼의 next 항목에 {{next}}변수값을 할당. 이문장에 의해 login()뷰가
POST 요청을 처리한 후, 즉 로그인이 성공한 경우에 {{next}} 변수로 지정된 URL로 이동 시켜줌.          
            <input type="hidden" name="next" value="{{ next }}">
        </div>
# 자바스크립트에 의해 Username 입력 요소에 커서를 위치시킴
        <script type="text/javascript">document.getElementById('id_username').focus();</script>
    </form>
</div>
{% endblock %}
```

## 함수형 login_required()를 클래스형으로쓸때 정의하기

```
# login_required() 함수는 함수에만 적용할수 있으므로 클래스형 뷰에서는 LoginRequireMixin 클래스를 상속받아
# 사용하면 login_required() 데코레이터 기능을 제공할 수 있음
class LoginRequiredMixin(object):
    # as_view() 메소드를 인스턴스 메소드가 아니라 클래스 메소드로 정의, as_view() 메소드는 항상 클래스 메소드로 정의
    @classmethod
    def as_view(cls, **initkwargs):
        # super() 메소드에 의해 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드가
        # view 변수에 할당
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        # view 변수, 즉 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드에 Login_required()
        # 기능을 적용하고 그 결과를 반환
        return login_required(view)
```