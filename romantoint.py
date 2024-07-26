def roman_to_integer(roman: str)->int:
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000

    }
    total = 0
    n = len(roman)
    
    for i in range(n):
        #Get the value of the current roman numeral
        current_value = roman_to_int[roman[i]]
        #check if there is a next character and if the current value is less than the next value
        if i + 1 < n and current_value < roman_to_int[roman[i+1]]:
            #Subtract the current value (for cases like IV, IX, etc)
            total -= current_value
        return total
    
    #Example usage
    roman_numeral = "MCMXCIV"
    result = roman_to_integer(roman_numeral)
    print("The integer value of the roman numeral {roman_numeral} is: {result} ")
    

