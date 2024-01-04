import random
select = [ "가위", "바위", "보"]
enemy=random.choice(select)



while True:
    user=input("가위 바위 보 중에서 하나를 입력하세요.")
    if user in select:
        break
    print("잘못된 입력입니다. 다시 입력하세요.")

if user=="가위" and enemy =="보" or \
user =="바위" and enemy=="가위" or\
user=="보" and enemy=="바위":
    print("이겼어요")
else:
    print("적이 이겼습니다. 넌 졌습니다.")