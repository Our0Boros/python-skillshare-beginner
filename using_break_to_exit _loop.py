### 01/05/2020
### Author: Omer Goder
### Using break to exit a loop

prompt = "\nDo you want to quit?\nIf so enter 'q'"
loop ="\nThis is loop at level: "
while True:
    while True:
        while True:
            level = 3
            print(loop + str(level))
            done = input(prompt)
            if done == 'q':
                break
        level = 2
        print(loop + str(level))
        done = input(prompt)
        if done == 'q':
            break
    level = 1
    print(loop + str(level))
    done = input(prompt)
    if done == 'q':
        break

