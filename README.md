# TODO_LIST

이 프로젝트는 Django Rest Framework를 사용하여 개발된 할일 목록 관리 앱입니다.

## API 기능

### 유저 기능

#### 회원가입

- POST /users/signup/: 새로운 회원을 등록합니다.

#### 로그인한 회원 정보 수정

- PUT /users/signup/: 로그인한 회원의 정보를 수정합니다.

#### 로그인한 회원 삭제

- DELETE /users/signup/: 로그인한 회원을 삭제합니다.

### 할일 목록 기능

#### 할일 목록 조회

- GET /todolist/: 할일 목록을 조회합니다.

#### 할일 추가

- POST /todolist/: 새로운 할일을 추가합니다.

#### 할일 상세 정보 조회

- GET /todolist/<int:todo_id>/: 특정 할일의 상세 정보를 조회합니다.

#### 할일 수정

- PUT /todolist/<int:todo_id>/: 특정 할일의 정보를 수정합니다.

#### 할일 삭제

- DELETE /todolist/<int:todo_id>/: 특정 할일을 삭제합니다.

### 인증

이 앱은 JWT(Json Web Token) 기반 인증을 사용합니다.
