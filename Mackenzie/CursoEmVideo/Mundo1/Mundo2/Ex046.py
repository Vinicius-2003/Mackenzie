from time import sleep
import emoji
for c  in range(10,-1,-1):
    sleep(1)
    print(c)
print(emoji.emojize(":fire:"),end='')
print('\033[1;31mFOGoOoO!\033[m',end='')
print(emoji.emojize(":fire:"))