# template


## blog templates
+ `&laquo;--` 는 html특수문자 << 를 의미
+ `--&raquo;` 는 html특수문자 >> 를 의미
+ `&amp;`는 html 특수문자 & 를 의미
+ `&bigtriangledown;`는 html 특수문자 &bigtriangledown; 의미
+ `&copy;`는 html 특수문자 &copy;를 의미

```
<h1>Blog List</h1>

{% if post in posts %}
    <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
    # 속성값을 "N d, Y 포맷으로 출력(ex) July 01, 2019)
    {{ post.modify_date|date:"N d, Y"}}
    <p>{{ post.description }}</p>
{% endif %}

<br/>

<div>
    <span>
    # page_obj는 장고의 Page 객체가 들어있는 컨텍스트 변수 현재페이지 기준으로
    	이전페이지가 있는지 확인 
        {% if page_obj.has_previous %}
    # pate_obj.previous_page_number 이전 페이지의 번호, 이전페이지 링크연결
            <a href="?page={{ pate_obj.previous_page_number }}">PreviousPage</a>
        {% endif %}
	# 현재 페이지 번호, 총페이지 개수를 의미
        Page {{ page_boj.number }} of {{ page_obj.paginator.num_pages }}
	# 다음 페이지 확인
        {% if page_obj.has_next %}
        # 다음페이지번호, 다음페이지 링크 연결
            <a href="?page={{ page_obj.next_page_number }}">NextPage</a>
        {% endif %}
    </span>
</div>
```
```
<h2>{{ object.title }}</h2>

<p class="other_posts">
# modify_date 컬럼 기준으로 이전객체를 반환, 즉 변경날짜가 현재 객체보다 오래된 객체가 있는지 확인
    {% if object.get_previous_by_modify_date %}
# get_previous_post 함수는 이전 객체포스트, get_absoulte_url 이전 객체를 지칭하는 URL 패턴반환
# URL링크 연결, &laquo 는 html특수문자 << 를 의미
    <a href="{{ object.get_previous_post.get_absoulte_url }}" title="View previous post">&laquo;--{{ object.get_previous_post }}</a>
    {% endif %}

    {% if object.get_next_by_modify_date %}
    | <a href="{{ object.get_next_post.get_absoulte_url }}" title="View next post">{{ object.get_next_post }}--&raquo;</a>
    {% endif %}
</p>

# modify_date 속성값을 "j F Y" 포맷으로 출력(ex) 12 July 2019)
<p class="date">{{ object.modify_date|date:"j F Y"}}</p>

<br/>

<div class="body">
# linebreaks 템플릿 필터는 \n (newline)을 인식
    {{ object.content|linebreaks }}
</div>
```

```
# {% now %} 템플릿 태그는 현재의 날짜와 시간을 원하는 포맷으로 출력 N d, Y (July 18, 2019)
<h1>Post Archives until {% now "N d, Y" %}</h1>
<ul>
# date_list 컨텍스트 변수는 DateQuerySet 객체 리스트를 담고있다, DateQuerySet은 QuerySet 객체
리스트에서 날짜 정보만 추출해 담고 있는 객체임.
    {% for date in date_list %}
# 메뉴를 한 줄에 보여주기위해 inline 해줌    
    <li style="display: inline;">    
        <a href="{% url 'blog:post_year_archive' date|date:'Y' %}">Year - {{ date|date:'Y' }}</a>
    </li>
    {% endfor %}
</ul>
<br/>
<div>
    <ul>
        {% for post in objects_list %}
# &nbsp; 빈칸을 출력하는 html 특수문자 
        <li>{{ post.modify_date|date:"Y-m-d" }}&nbsp;&nbsp;&nbsp;
            <a href="{{ post.get_absolute_url }}"><strong>{{ post.title }}</strong></a>
        </li>
    </ul>
</div>
```


```
# 
<h1>Post Archives for {{ year|date:"Y" }}</h1>

<ul>
    {% for date in date_list %}
    <li style="display: inline;">
# 월 메뉴는 "F" July 형식의 텍스트로, 해당 연월에 생성 또는 수정된 modify_date 포스트를 보여주는 URL링크  
        <a href="{% url 'blog:post_month_archive' year|date:'Y' date|date:'b' %}">
            {{ date|date:"F"}} 
        </a>
    </li>
    {% endfor %}
</ul>

<br/>>

<div>
    <ul>
        {% for post in object_list %}
        <li>{{ post.modify_date|date:"Y-m-d"}}&nbsp;&nbsp;&nbsp;
            <a href="{{ post.get_absolute_url }}"><strong>{{ post.title }}</strong></a>
        </li>
    </ul>
</div>
```