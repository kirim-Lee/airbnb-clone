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