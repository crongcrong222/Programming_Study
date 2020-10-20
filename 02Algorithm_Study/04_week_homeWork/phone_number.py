def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print("p1",p1,"p2",p2)
        if p2.startswith(p1):
            return False
    return True

#  B.startswith(A) 내가 찾고자 하는 문자열 A가 문자열 B 

solution(["119", "97674223", "1195524421"])
