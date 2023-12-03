#ideally checks if result is an integer, ie. box_v ==0 and adds the values if result is an integer (PROB DOESNT WORK) 
def sums (box_v, box_c):
  result = box_v + box_c
  if isinstance(result, int):
    print(result)   
  else:
    print(sum(result))

# List of common factors to check for factorising 
def factor_check([box_c]{box_v}):
    factors = [
        f'sin([box_c]{box_v})', f'ln([box_c]{box_v})', f'tan([box_c]{box_v})', f'cos([box_c]{box_v})',
        f'arccos([box_c]{box_v})', f'arcsin([box_c]{box_v})', f'arctan([box_c]{box_v})', f'e**([box_c]{box_v})', f'x**([box_c]{box_v})', f'(base)**([box_c]{box_v})
    ]

    for factor in factors:
        if factor in str([box_c]{box_v}):
            return factor

    return None
  #checks for common factors and factorising
def factorize([box_c]{box_v}):
    factors = [
        f'sin([box_c]{box_v})', f'ln([box_c]{box_v})', f'tan([box_c]{box_v})', f'cos([box_c]{box_v})',
        f'arccos([box_c]{box_v})', f'arcsin([box_c]{box_v})', f'arctan([box_c]{box_v})', f'e**([box_c]{box_v})', f'x**([box_c]{box_v})'
    ]

    for factor in factors:
        if factor in str([box_c]{box_v}):
            common_factor = factor
  # Attempting to factorize by finding by the common factor
            expression = str([box_c]{box_v}).replace(common_factor, '')  
            if expression.startswith('*'):  
                expression = expression[1:] 

            return expression.strip()  
    
    return str([box_c]{box_v})  
WIP
