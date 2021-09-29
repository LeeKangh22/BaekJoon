a, b = map(int, input().split())

#최대 공약수는 유클리드 호제법 사용
#숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b 의최대 공약수 는 a 와 b 의 최대 공약수 가 같다는 것을 의미
def gcd(a, b):
    while b > 0:
        a, b = b , a % b
    return a
print(gcd(a, b))
#최소 공배수는 두 수의 곱에서 최대 공약수를 나누면 생긴다.
print(int(a * b / (gcd(a, b))))
