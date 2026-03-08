# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
import random
LOWER_LIMIT = 1
UPPER_LIMIT = 100

def guess_the_number():
    final_answer = random.randint(LOWER_LIMIT+1,UPPER_LIMIT-1)
    adjusted_lower_limit = LOWER_LIMIT
    adjusted_upper_limit = UPPER_LIMIT
    while True:
        me_answer = int(input(f"範圍在{adjusted_lower_limit}~{adjusted_upper_limit} 請輸入您的數字:"))
        if me_answer == final_answer:
            print(f"恭喜中獎，正確答案就是{final_answer}")
            break
        else:
            if me_answer > final_answer :
                print("太大了!")
                adjusted_upper_limit = me_answer
            else:
                print("太小了")
                adjusted_lower_limit = me_answer
guess_the_number()

    








