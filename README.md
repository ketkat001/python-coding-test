# - 이것이 코딩테스트다 with Python

## 그리디 알고리즘

### 정의 :

​	그리디 알고리즘 (욕심쟁이 알고리즘, Greedy Algorithm)은 단순하지만 강력한 해결 방법이다.  어떠한 문제가 있을 때 단순 무식하게 탐욕적으로 문제를 푸는 알고리즘. 여기서의 탐욕의 뜻은 "현재 상황에서 지금 당장 좋은 것만 고르는 방법"을 의미.

​	그리디 알고리즘으로 문제를 해결할 경우 그 해법이 정당한지 검토해야 한다. 



### 문제 : 문제 제목 | 문제 경로

#### Q.01 모험가 길드 | [모험가 길드.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q01-모험가길드.py)

#### Q.02 곱하기 혹은 더하기 | [곱하기 혹은 더하기.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q02-곱하기혹은더하기.py)

#### Q.03 문자열 뒤집기 | [문자열 뒤집기.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q03-문자열뒤집기.py)

#### Q.04 만들 수 없는 금액 | [만들 수 없는 금액.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q04-만들수없는금액.py)

#### Q.05 볼링공 고르기 | [볼링공 고르기.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q05-볼링공고르기.py)

#### Q.06 무지의 먹방 라이브 | [무지의 먹방 라이브.py](https://github.com/ketkat001/python-coding-test/blob/master/그리디알고리즘/Q06-무지의먹방라이브.py)



## 구현

### 정의 : 

​	머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정. 코딩을 배운 기간이 짧을수록 구현단계에서 어려움을 겪을 가능성이 높음. 



### 문제 : 문제 제목 | 문제 경로

#### Q.07 럭키스트레이트 | [럭키스트레이트 .py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q07-럭키스트레이트.py)

#### Q.08 문자열 재정렬 | [문자열 재정렬 .py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q08-문자열재정렬.py)

#### Q.09 문자열 압축 | [문자열 압축.py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q09-문자열압축.py)

#### Q.10 자물쇠와 열쇠 | [자물쇠와 열쇠.py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q10-자물쇠와열쇠.py)

#### Q.11 뱀 | [뱀 .py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q11-뱀.py)

#### Q.12 기둥과 보 설치 | [기둥과 보 설치py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q12-기둥과보설치.py)

#### Q.13 치킨배달 | [치킨배달.py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q13-치킨배달.py)

#### Q.14 외벽점검 | [외벽점검.py](https://github.com/ketkat001/python-coding-test/blob/master/구현/Q14-외벽점검.py)



## DFS  | BFS

### 정의:

- 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정. 대표적인 탐색 알고리즘으로 DFS(깊이 우선 탐색) 와 BFS(넓이 우선 탐색)가 있음. DFS와 BFS를 이해하려면 기본 자료구조인 스택과 큐에 대한 이해가 전제되어야 함.

  

- 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조. 그 중 스택과 큐는 자료구조의 기초 개념.
- 재귀함수: DFS와 BFS를 구현하려면 재귀 함수도 이해하고 있어야 한다. 재귀함수란 자기 자신을 다시 호출하는 함수.



### DFS

#### 정의:

​	DFS는 Depth-First Search, 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

#### 동작 원리:

- 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
- 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
- 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

*** '방문 처리' 는 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것을 의미한다. 방문 처리를 함으로써 각 노드를 한 번씩만 처리할 수 있다.



### BFS

#### 정의:

​	BFS Breath First Search 알고리즘은 '너비 우선 탐색' 이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다.

DFS는 가장 멀리 있는 노드를 최우선으로 탐색하는 방식으로 동작한다고 했지만 BFS는 그 반대로 동작한다.

#### 동작 원리:

- 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
- 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
- 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.



### 문제: 문제 제목 | 문제 경로

#### Q.015 특정 거리의 도시찾기 | [특정 거리의 도시찾기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q15-특정거리의도시찾기.py)

#### Q.016 연구소 | [연구소.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q16-연구소.py)

#### Q.017 경쟁적 전염 | [경쟁적 전염.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q17-경쟁적전염.py)

#### Q.018  괄호 변환| [괄호 변환.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q18-괄호변환.py)

#### Q.019 연산자 끼워넣기 | [연산자 끼워넣기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q19-연산자끼워넣기.py)

#### Q.020 감시 피하기 | [감시 피하기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q20-감시피하기.py)

#### Q.021 인구 이동 | [인구 이동.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q21-인구이동.py)

#### Q.022 블록 이동하기 | [블록 이동하기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2C BFS 문제/Q22-블록이동하기.py)