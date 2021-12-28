# basic_calculator.py
print('basic_calculator.py')


##################################################################################################
########## CALCULATOR WITH INPUT CHECKING=========================================

################# functions ################################
def input_number(which_num):
    check_val=False
    try:
        num_ip = float(input(f'Enter {which_num} number: ')) #check input can be converted to a number
        #return num_ip, True
    except:
        print('Please enter a number')
        num_ip = None
        check_val = True
    return num_ip, check_val

def input_operator():
    op_ip = input('Enter operator: a (add), s (subtract, m (multiply), d (divide) or x to (exit): ')
    if op_ip in ['a','s','m','d','x']: #check input as required
        return op_ip, False
    else:
        return op_ip, True

def do_calc(op_in,f_num,s_num):
    if op_in == 'a':
        result , op_out = (f_num + s_num), 'added to'
    elif op_in == 's':
        result , op_out = (s_num - f_num), 'subtracted from'
    elif op_in == 'm':
        result , op_out = (f_num * s_num), 'multiplied by'
    elif op_in == 'd':
        if s_num == 0:
            print('Unable to divide by 0, please try again') #check if dividing by zero
            result , op_out = None, None
        else:
            result , op_out = (f_num / s_num), 'divided by'
    return result, op_out


#################### main #########################
exit_no = True
while exit_no:    #checks if exit (x) has been entered
    #enter operator or exit
    check_operator = True
    while check_operator:
        my_operator, check_operator = input_operator()
        if my_operator == 'x':
            exit_no = False
    #enter first usernumber
    check_value=True
    while check_value and exit_no:
        first_num, check_value = input_number('First')
        #print('debugA', first_num, check_value)
    #enter second number
    check_value=True
    while check_value and exit_no:
        second_num, check_value = input_number('Second')
    #enter operator or exit
    if exit_no:
        result, op_out = do_calc(my_operator, first_num, second_num)
        if result != None:
            print(f'{first_num} {op_out} {second_num} is: {result}')
