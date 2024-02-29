
answer1 = int(input("Hello. This is a conversion number system. If you want to convert Roman numbers to normal numbers, press 1. If you want to convert normal numbers to Roman, press 2. "))

def int_to_roman(user_input):

        final_answer = str()

        for i in range(user_input):
            if user_input >= 1000:
                final_answer = final_answer + "M"
                user_input -= 1000
            elif user_input >= 900:
                final_answer = final_answer + "CM"
                user_input -= 900
            elif user_input >= 500:
                final_answer = final_answer + "D"
                user_input -= 500
            elif user_input >= 400:
                final_answer = final_answer + "CD"
                user_input -= 400
            elif user_input >= 100:
                final_answer = final_answer + "C"
                user_input -= 100
            elif user_input >= 90:
                final_answer = final_answer + "XC"
                user_input -= 90
            elif user_input >= 50:
                final_answer = final_answer + "L"
                user_input -= 50
            elif user_input >= 40:
                final_answer = final_answer + "XL"
                user_input -= 40
            elif user_input >= 10:
                final_answer = final_answer + "X"
                user_input -= 10
            elif user_input == 9:
                final_answer = final_answer + "IX"
                user_input -= 9
            elif user_input == 8:
                final_answer = final_answer + "VIII"
                user_input = user_input - 8
            elif user_input == 7:
                final_answer = final_answer + "VII"
                user_input = user_input - 7
            elif user_input == 6:
                final_answer = final_answer + "VI"
                user_input -= 6
            elif user_input == 5:
                final_answer = final_answer + "V"
                user_input -= 5
            elif user_input == 4:
                final_answer = final_answer + "IV"
                user_input -= 4
            elif user_input == 3:
                final_answer = final_answer + "III"
                user_input -= 3
            elif user_input == 2:
                final_answer = final_answer + "II"
                user_input -= 2
            elif user_input == 1:
                final_answer = final_answer + "I"
                user_input -= 1
            else:
                break

        print(f"The number you wrote in roman numbers is: {final_answer}")

def roman_to_int(numeral):
        
        final_answer = 0
        
        if "CM" in numeral:
            final_answer += 900
            numeral = numeral.replace("CM", "")
        if "CD" in numeral:
            final_answer += 400
            numeral = numeral.replace("CD", "")
        if "XC" in numeral:
            final_answer += 90
            numeral = numeral.replace("XC", "")
        if "XL" in numeral:
            final_answer += 40
            numeral = numeral.replace("XL", "")
        if "IX" in numeral:
            final_answer += 9
            numeral = numeral.replace("IX", "")
        if "IV" in numeral:
            final_answer += 4
            numeral = numeral.replace("IV", "")
        
        for i in numeral:
            if i == "M":
                final_answer += 1000
            elif i == "D":
                final_answer += 500
            elif i == "C":
                final_answer += 100
            elif i == "L":
                final_answer += 50
            elif i == "X":
                final_answer += 10
            elif i == "V":
                final_answer += 5
            elif i == "I":
                final_answer += 1
        
        print(f"The roman numerals you entered translates to: {final_answer} !")

if answer1 == 1:
    numeral_input = input("Enter the roman numeral you want to convert: ")

    

    roman_to_int(numeral_input)

elif answer1 == 2:
    user_input2 = int(input("Write the number you want to convert to roman number: "))

    int_to_roman(user_input2)

else:
    print("You have entered the wrong number or character")
