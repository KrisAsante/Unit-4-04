# Created by: Chris Asante
# Created on: 1-April-2019
# Created for: ICS3U
# Daily Assignment – Unit 4-04
# This program prints out an average of a grade percentage


def calculate(level):
    
    if level == "4+":
        return 97.5
        
    elif level == "4":
        return 90.5
        
    elif level == "4-":
        return 83
        
    elif level == "3+":
        return 78
        
    elif level == "3":
        return 74.5
        
    elif level == "3-":
        return 71
        
    elif level == "2+":
        return 68
        
    elif level == "2":
        return 64.5
        
    elif level == "2-":
        return 61
        
    elif level == "1+":
        return 58
        
    elif level == "1":
        return 54.5
        
    elif level == "1-":
        return 51
        
    elif level == "R":
        return 30
        
    elif level == "NE":
        return 0
        
    else:
        return -1

level = str(input("Enter your mark (4+ to NE): "))
answer = calculate(level) 
print(answer)
