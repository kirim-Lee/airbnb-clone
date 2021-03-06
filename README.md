## 설치

### python 설치

- brew install python3

### pipenv 설치

- brew install pipenv

### 가상환경 생성

- 작업폴더에서 pipenv --three (파이썬 3를 사용하는 가상환경을 만들라는 뜻)
- Pipfile이 생성됨

### django 설치

- 작업폴더에서 pipenv shell 로 가상환경에 진입
- pipenv install Django 장고 설치
- 설치확인 django-admin을 실행해서 잘 나오는지 확인 (which django-admin)

## django project 생성

- django-admin startproject 프로젝트명 ... 으로 documentation 되어있지만 다른 방식으로 작업
- **django-admin startproject config 입력 - 이렇게 하는 이유 확장이 용이해짐 config 폴더를 생성**
- config/config 의 config 폴더를 밖으로 이동

### Formatter

- pipenv install black --dev --pre

### linter

- flake8

## django project 실행

- python manage.py runserver: 서버를 시작
- python manage.py migrate : 처음 실행시 어드민을 접속할 수 있게됨
- python manage.py createsuperuser : 관리자를 만듬
- python manage.py makemigrations : 마이그레이션 , 데이터 형태가 바뀔때
- migration => migrate

## django model 생성

- django-admin startapp [name]
- 이 프로젝트에서는: rooms, users, review, conversations, list, reservations 을 생성함

## django app 으로 부터

### 각앱의

- admin.py 어드민에 보이고 싶은것
- views.py 페이지
- models.py 데이터모델

### config

- urls.py URL을 설정

## django 팁

### user 덮어쓰기

- https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model

### 기본 제공 어드민 화면 사용하기 (리스트)

- from django.contrib.auth.admin import UserAdmin
- Custom 클래스에 상속해줌 (users/admin.py 참조)
- **class CustomUserAdmin(UserAdmin):**

### admin 리스트에 항목 정의

- list_display("param name",...)
- https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

### admin 리스트 필터링

- list_filter("param name", ...)
- https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter

### admin view page fieldset

- https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets

### foreignKey / ManyToManyField 로 연결된 객체 접근

- [name]\_set 으로 접근
- obj.[foreignParam]\_set.all()
- model 설정시 related_name 으로 set대신 사용가능
- 접근 관계에 대해 : A에서 B를 foreignKey로 지정하면 B에서 A를 \_set으로 접근할수 있다

### admin.TabularInline

- foreignKey 를 가지고 있는 모델을 편하게 등록할 수 있도록 설정
- ex 룸 등록 시 포토를 한번에 등록이 가능
- fd27abd34774ac81f0057a9c65750d34ef7323a1 커밋 참조

### Base Command 사용하기

- https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/
- app 내부에서 (각 폴더에서) 다음과 같은 구조로 파일을 생성한다.

```structure
- rooms
  - management
    - commands
      - __init__.py
      - [사용할 명령어].py
```

- [사용할 명렁어].py

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  def handle(self, *args, **options):
    # 사용할 명령 입력
```

- 사용: python manage.py [사용할명령어]
- rooms/management/commands 참조
- users/management/commands 참조
- django-seed lib 사용

## django Views / urlpatterns

- https://docs.djangoproject.com/ko/3.1/intro/tutorial03/
- config/urls.py 에서 직접 등록이 가능하다.

```python
from django.urls import path, include

urlpatterns = [
    # path / 일때 core/urls.py 를 불러오고 namespace는 core 로 사용하기로 한다
    # namespace를 사용하면 core/urls.py 에 app_name='core'로 설정해주어야 한다.
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]
```

- core/urls.py

```python
from django.urls import path
from rooms import views as room_views

app_name = "core"

# path "/" 일때 room/views.py 의 all_rooms를 사용하도록 함
urlpatterns = [path("", room_views.all_rooms, name="home")]
```

### template 경로 변경

- template을 root로 수정
- config/settings.py 수정

```python
TEMPLATES = [
    {
        ...,
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        ...
    }
```

### 템플릿 문법

- https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#ref-templates-builtins-tags
- built-in filter
  - https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference

#### 공통 템플릿
- extends 와 block을 이용해 구성할 수 있다.
- home.html
```python
# layout 
{% extends 'base.html' %}
{% block content %}
# 여기에 컨텐츠를 등록함
{% endblock %}
```
- base.html
```python
<html>
<head />
<body>
{%block content %}
# 여기에 컨텐츠가 입력된다.
{% endblock %}
</body>
</html>
```

### django paginator
- https://docs.djangoproject.com/en/3.1/ref/paginator/#django.core.paginator.Page

### Class based list view
- https://docs.djangoproject.com/en/3.1/ref/class-based-views/
- https://ccbv.co.uk/