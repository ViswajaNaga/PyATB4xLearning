# formating number
number = 3.16159265359
Formatted_number = f"{number:.4f}"
print(Formatted_number)  # 3.1416
# 3.1416- Rounding off is happening for last digit
# as 4th digit is 5 and fifth digit is 9, last digit is rounded off to 6

Formatted_number = f"{number:.2f}"
print(Formatted_number)  # 3.16

Formatted_number = f"{number:.1f}"
print(Formatted_number)  # 3.2

# Format String
num=90
print("this is the number you are working with",f"{num}")  # this is the number you are working with 90


