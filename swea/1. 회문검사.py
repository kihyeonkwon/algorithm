a = input()


def palindrome(a) :
    b= a[::-1]
    if b==a:
        print(a)
        print('입력하신 단어는 회문(Palindrome)입니다.')


palindrome(a)