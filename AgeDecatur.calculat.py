# Created by ARIT DEY
print("     🚹 created by ARIT DEY 🚹\n") 

print ("enter your age here -->\n")
try:
    age=int (input())
except ValueError:
    print("  ⚠️please enter your age first!")

try :
    year=age
    season=age * 4
    month=age * 12
    week=age * 52
    day=age * 365
    hour=age * 365 * 24
    minute=age * 365 * 24 * 60
    seconde=age * 365 * 24 * 60 * 60

    print("your age is:")
    print("totale year =",year)
    print("totale season =",season)
    print("totale month =",month)
    print("totale week =",week)
    print("totale day =",day)
    print("totake hour =",hour)
    print("totale minute =",minute)
    print("totale second =",seconde)

except NameError :
    print ("")
