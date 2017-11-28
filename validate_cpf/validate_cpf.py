def validate_cpf(cpf):
    format_cpf = cpf.replace('.','').replace('-','')
    
    if not len(format_cpf) == 11:
        return False

    if not validate_first_number(format_cpf):
        return False
    
    if not validate_second_number(format_cpf):
        return False
    
    return True

def validate_first_number(cpf):
    first_digit = int(cpf[-2])
    the_first_nine_digits = cpf[:9]
    list_ten_to_two = reversed(range(2, 11))
    sum_cpf = 0

    for cpf, mult in zip(the_first_nine_digits, list_ten_to_two):
        sum_cpf += int(cpf) * mult

    rest = sum_cpf * 10 % 11
  
    if rest != first_digit:
        return False
    
    return True

def validate_second_number(cpf):
    second_digit = int(cpf[-1])
    the_first_ten_digits = cpf[:10]
    list_eleven_to_two = reversed(range(2, 12))
    sum_cpf = 0

    for cpf, mult in zip(the_first_ten_digits, list_eleven_to_two):
        sum_cpf += int(cpf) * mult

    rest = sum_cpf * 10 % 11
    
    if not rest == second_digit:
        return False

    return True
