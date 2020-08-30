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



## DFS  | BFS 탐색 알고리즘

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

#### Q.015 특정 거리의 도시찾기 | [특정 거리의 도시찾기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q15-특정거리의도시찾기.py)

#### Q.016 연구소 | [연구소.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q16-연구소.py)

#### Q.017 경쟁적 전염 | [경쟁적 전염.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q17-경쟁적전염.py)

#### Q.018  괄호 변환| [괄호 변환.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q18-괄호변환.py)

#### Q.019 연산자 끼워넣기 | [연산자 끼워넣기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q19-연산자끼워넣기.py)

#### Q.020 감시 피하기 | [감시 피하기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q20-감시피하기.py)

#### Q.021 인구 이동 | [인구 이동.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q21-인구이동.py)

#### Q.022 블록 이동하기 | [블록 이동하기.py](https://github.com/ketkat001/python-coding-test/blob/master/DFS%2CBFS문제/Q22-블록이동하기.py)



## 정렬 알고리즘

### 정의:

​	정렬(Sorting)이란, 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.

### 종류:

####  1) 선택 정렬:

​	데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복.

​	가장 원시적인 방법으로 매번 '가장 작은 것을 선택' 한다는 의미에서 **선택 정렬(Selection Sort)** 알고리즘이라고 한다.

##### 선택 정렬의 시간복잡도

​	선택 정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다. 매번 가장 작은 수를 찾기 위해서 비교 연산이 필요하다. 이를 빅오표기법으로 간단히 O(N^2)이라고 표현할 수 있다.

##### 선택 정렬의 소스코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)
```



#### 2) 삽입 정렬:

​	삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 **삽입 정렬(Insertion Sort)**이라고 부른다. 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.

##### 삽입 정렬의 시간 복잡도

​	삽입 정렬의 시간복잡도는 O(N^2)이지만, 현재 리스트의 데이터가 거의 정렬되어 있을 때, 최선의 경우 O(N)의 시간복잡도를 가진다. 그러므로 거의 정렬된 리스트가 주어질 경우 삽입 정렬을 이용하는 것이 정답 확률을 높일 수 있다.

##### 삽입 정렬의 소스코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
```



#### 3) 퀵 정렬:

​	정렬 알고리즘 중에 가장 많이 사용되는 알고리즘. 퀵 정렬과 병합 정렬은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이다.

​	퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.

##### 퀵 정렬의 시간 복잡도

​	퀵 정렬의 시간복잡도는 평균적으로 O(NlogN)이다. 하지만 최악의 경우 시간 복잡도는 O(N^2)으로 데이터가 모두 정렬되어 있는 경우 매우 느리게 작동한다. 앞서 말한 삽입정렬의 경우 데이터가 정렬되어 있는 경우 매우 빠르게 동작한다고 했지만 퀵 정렬은 그 반대로 데이터가 정렬되어 있지 않은 경우에 더 빠르게 동작한다.

##### 퀵 정렬의 소스코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)
```

- 파이썬의 장점을 살린 퀵 정렬 소스코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```



### 문제 : 문제 제목 | 문제 경로

#### Q.023 국영수 | [국영수](https://github.com/ketkat001/python-coding-test/blob/master/정렬알고리즘/Q23-국영수.py)

#### Q.024 안테나 | [안테나](https://github.com/ketkat001/python-coding-test/blob/master/정렬알고리즘/Q24-안테나.py)

#### Q.025 실패율 | [실패율](https://github.com/ketkat001/python-coding-test/blob/master/정렬알고리즘/Q25-실패율.py)

#### Q.026 카드 정렬하기 | [카드 정렬하기](https://github.com/ketkat001/python-coding-test/blob/master/정렬알고리즘/Q26-카드정렬하기.py)

