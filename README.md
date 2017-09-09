# Project 1010235 back-end API Server

url : 1010235.ap-northeast-2.elasticbeanstalk.com

##### API

URI | Method | Content | Params
----| ------ | ------- | ------
`/create` | `POST` | 번호를 생성합니다. | `number(int)`
`/send` | `POST` | 메시지를 보냅니다. | `number(int)`, `msg(int)`
`/list/<number>` | `GET` | 해당 번호의 모든 메시지 |
`/list/<number>/new` | `GET` | 새로운 메시지 목록 |