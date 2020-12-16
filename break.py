'''while True:
    command = input("Type 'exit' to exit: ")
    if command == 'exit':
        break
'''

times = int(input('How many times do i have to tell you'))
for i in range(times):
    print('Clean your room')
    if i >= 4:
        print('do you even listen')
        break