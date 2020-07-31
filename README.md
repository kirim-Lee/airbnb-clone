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
- [name]_set 으로 접근
- obj.[foreignParam]_set.all()
- model 설정시 related_name 으로 set대신 사용가능
- 접근 관계에 대해 : A에서 B를 foreignKey로 지정하면 B에서 A를 _set으로 접근할수 있다