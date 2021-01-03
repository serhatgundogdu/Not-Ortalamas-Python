
grades = []

def stringToBold(val):
    return "\033[1m" + str(val) + "\033[0m"

def findNote(val):
    if val <= 100 and val>= 80:
        return "A"
    else:
        return "F"

def setInput(val):

    val = int(val)
    if(type(val) != int):
        print("Write a Input not String")
        x = input("Notunuzu giriniz: ")
        setInput(x)
    if(val != -1000):
        if val <= 100 and val>= 0:
            grades.append(val)
            print("The letter grade equivalent of ",stringToBold(val)," is ",stringToBold(findNote(val)),".")
            x = input("Notunuzu giriniz:  ")
            setInput(x)
        else:
            print("Invalid value: ",stringToBold(val))
            x = input("Notunuzu giriniz: ")
            setInput(x)
    else:
        totalNote = 0
        for x in grades:
            totalNote+=x
        TotalGrade = totalNote/len(grades)
        print("Not ortalamanız: ",stringToBold(TotalGrade))
            

        
x = input("Notunuzu giriniz: ")
setInput(x)