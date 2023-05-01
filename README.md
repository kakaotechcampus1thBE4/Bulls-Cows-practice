# Description
해당 Repository는 카카오 테크 캠퍼스 1기 백엔드 4조 Git 실습을 위해 작성되었습니다.

Bulls and cows는 숫자를 추측하는 게임입니다. 이 게임은 두 명 이상의 참가자가 필요하며, 한 명이 비밀로 선택한 숫자를 다른 참가자들이 추측하는 게임입니다.
우리나라에서는 숫자야구로도 잘 알려져있는 게임입니다.
See [Example](https://www.mathsisfun.com/games/bulls-and-cows.html)

## Rules
Bulls and cows 게임의 규칙은 다음과 같습니다:
* 숫자는 0에서 9 사이의 서로 다른 네 자리 숫자를 컴퓨터가 생성합니다.
* 유저는 매 순서마다 0에서 9 사이의 서로 다른 네 자리 숫자를 제시합니다.
* 제시한 숫자 중에서 비밀 숫자와 숫자와 위치가 모두 일치하는 숫자가 있는 경우 "3 bulls"라는 힌트를 받습니다.
* 제시한 숫자 중에서 비밀 숫자와 숫자는 일치하지만 위치가 다른 경우 "3 cows"라는 힌트를 받습니다.
* 유저는 이러한 힌트를 토대로 계속해서 숫자를 추측하며, 비밀 숫자를 맞히는 사람이 이깁니다.

### Installation
```shell
$ git clone {repo url}
$ cd {reponame}
$ pip install -r requirements.txt
```

### How to Start

```shell
$ python main.py
```

### Dependencies
- Python >= 3.x


### Features
- TBA


