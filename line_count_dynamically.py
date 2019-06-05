while(True):
    user_string = ''
    break_string = ''
    while(True):
        break_string = input()
        if break_string == 'done':
            break
        user_string = user_string + '\n' + break_string
    user_string_list = user_string.split('\n')
    print(len(user_string_list)-1)
    close = input('want to exit: ')
    if close == 'exit':
        break
        
