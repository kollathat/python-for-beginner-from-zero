import time

count = 0
atk = 50
while atk > 0:
    print(f'ATK remaining... {str(atk)}.')
    atk -= 1
    if atk < 10 and count != 3:
        atk = atk + 10
        print('Add more 10 ATK(s)')
        count += 1
        print(f'Added ATK {str(count)} times.')

    time.sleep(0.5)
    
