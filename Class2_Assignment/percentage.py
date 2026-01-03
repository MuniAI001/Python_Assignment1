from All_functions import allfunctions

Subject1=int(input("Subject1 :"))
Subject2=int(input("Subject2 :"))
Subject3=int(input("Subject3 :"))
Subject4=int(input("Subject4 :"))
Subject5=int(input("Subject5 :"))
Marks=[Subject1,Subject2,Subject3,Subject4,Subject5]

allfunctions.percentage(*Marks)

'''
Output:
(.venv) PS C:\AI_Learing_Folder\Week2\Class2_Assignment> python percentage.py
Subject1 :80
Subject2 :85
Subject3 :90
Subject4 :95
Subject5 :100
Total : 450
Percentage :  90.0
'''