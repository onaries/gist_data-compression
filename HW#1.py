from operator import itemgetter
codes={}

# 알파벳 카운트
def frequency(string):
    # Dictionary 타입 변수 초기화
    freq = {}

    # 각 문자별
    for word in string:
        # 문자별 개수 카운트
        # get(key, default=None)
        freq[word] = freq.get(word, 0) + 1

    return freq


# 정렬
def sort(freq):
    # Dictionary의 Key 가져오기
    words = freq.keys()

    # tuple이 들어갈 리스트 초기화
    tuples = []

    # Dictionary의 Key
    for word in words:
        # 리스트에 튜플 추가
        tuples.append((freq[word], word))

    # 리스트 정렬
    tuples.sort()

    # 반환(튜플이 들어간 리스트)
    return tuples


# 트리 생성
def buildTree(tuples):
    #
    while len(tuples) > 1:
        # 확률이 제일 낮은 2개 선택
        leastTwo = tuple(tuples[0:2])

        # 나머지
        theRest = tuples[2:]

        # 확률이 제일 낮은 2개에서 빈도수를 더함
        combFreq = leastTwo[0][0] + leastTwo[1][0]

        # 새로운 리스트 생성
        tuples = theRest + [(combFreq, leastTwo)]

        # 리스트 정렬 (앞에 있는 숫자를 이용하여)
        tuples.sort(key=itemgetter(0))

    # 반환되는 값은 하나의 튜플
    return tuples[0]


def trimTree(tree):
    # p는 알파벳
    p = tree[1]

    # p가 문자열 타입이면
    if type(p) == type(''):

        # p를 반환
        return p

    # 아니면
    else:

        # 재귀함수
        return (trimTree(p[0]), trimTree(p[1]))

# 코드 할당
def assignCodes(nodes, pat=''):
    global codes
    if type(nodes) == type(''):
        codes[nodes] = pat
    else:
        assignCodes(nodes[0], pat+'0')
        assignCodes(nodes[1], pat+'1')


# 데이터 입력
def inputData(data):
    global tree
    tree = trimTree(buildTree(sort(frequency(data))))
    assignCodes(tree)
    print('input the data string : ', data)
    print('complete assign code ')


# 인코딩
def encode(string):
    global codes
    output = ''
    for ch in string:
        output += codes[ch]
    return output


# 디코딩
def decode(tree, s):
    output = ''
    p = tree
    for b in s:
        if b == '0':
            p = p[0]
        else:
            p = p[1]

        if type(p) == type(''):
            output += p
            p = tree
    return output