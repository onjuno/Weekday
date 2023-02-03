# Olle Nordlander - olno8946

dagarna = [31,28,31,30,31,30,31,31,30,31,30,31]
veckodagar = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


year = int(input("Year: "))
while year < 1583 or year > 9999:
    print ("Out of allowed range 1583 to 9999")
    year = int(input("Year: "))

skottor = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if skottor:
    dagarna[1] = 29

month = int(input("Month: "))
while month < 1 or month > 12:
    print ("Out of allowed range 1 to 12")
    month = int(input("Month: "))

month_max = dagarna[month - 1]

day = int(input("Day: "))
while day < 1 or day > month_max:
    print("Out of allowed range 1 to " + str(month_max))
    day = int(input("Day: "))

if month == 1 or month == 2:
    month += 12
    year -=1

weekday = (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7

namndag = veckodagar[weekday]

print("It is a " + namndag)
