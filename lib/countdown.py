import time

def countdown(count):
    while count > 0:
        print(f'{count} SECOND(S)!')
        count -= 1
    print("HAPPY NEW YEAR!")
        
def countdown_with_sleep(num):
    while num > 0: 
        print(f'{num} SECOND(S)!')
        time.sleep(1)
        num -= 1
    print("HAPPY NEW YEAR!")
        