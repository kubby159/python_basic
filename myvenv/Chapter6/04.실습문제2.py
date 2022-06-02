#docstring: 설명문
#문자열 포메팅

def printSumAvg(x,y,z):
    '''
    세개의 수를 받아 합계와 평균을 반환하는 함수.
    '''
    sum = x+y+z
    avg = int(sum/3)
    print(f'합계: {sum}')
    print(f'평균: {avg}')


printSumAvg(10,20,30)