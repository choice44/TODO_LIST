# TODO_LIST
내일배움캠프 장고 심화 개인과제입니다.
djangorestframework 시리얼라이저, 모델 쿼리셋 사용했습니다.
users 와 todolist 앱이 있고, 각각 회원가입,로그인 기능과 할일 작성 기능을 합니다.
로그인은 JWT 기반 인증을 사용합니다.

/users/signup/ 경로로 POST 요청을 보내면 회원가입을 할 수 있습니다.
/users/signup/ 경로로 PUT 요청을 보내면 로그인한 회원의 정보를 수정할 수 있습니다.
/users/signup/ 경로로 DELETE 요청을 보내면 로그인한 회원을 삭제할 수 있습니다.

/todolist/ 경로로 GET 요청을 보내면 할일 목록을 불러옵니다.
/todolist/ 경로로 POST 요청을 보내면 새로운 할일을 생성합니다.
/todolist/<int:todo_id>/ 경로로 GET 요청을 보내면 할일의 상세정보를 불러옵니다.
/todolist/<int:todo_id>/ 경로로 PUT 요청을 보내면 할일의 상세정보를 수정합니다.
/todolist/<int:todo_id>/ 경로로 PUT 요청을 보내면 할일을 삭제합니다.
