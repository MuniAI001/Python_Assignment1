class allfunctions():
    def Subfields():
        subflds=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing',
    'Natural Language Processing']
        print ("Sub-fields in AI are:")
        for i in subflds:
            print(i)
      
    def OddEven():
        inp=int(input('Enter a number: '))
        if inp%2==0:
            print(f'{inp} is even number')
        else:
            print(f'{inp} is odd number')
            
    def Elegible(genter,age):
        if genter.lower() == "male" and age > 24:
            print("Eligible")
        elif genter.lower() == "female" and age > 21:
            print("Eligible")
        else:
            print("Not Eligible")
    
    def percentage(*Args):
        Total = 0
        # Subject1=int(input("Subject1 :"))
        # Subject2=int(input("Subject2 :"))
        # Subject3=int(input("Subject3 :"))
        # Subject4=int(input("Subject4 :"))
        # Subject5=int(input("Subject5 :"))
        # Marks=[Subject1,Subject2,Subject3,Subject4,Subject5]
        for i in Args:
            Total = Total + i
        print("Total :",Total)
        print("Percentage : ", Total/5)
            
    def triangle():
        Height= int(input('Height:'))
        Breadth= int(input('Breadth:'))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", (Height*Breadth)/2)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth2= int(input('Breadth2:'))
        print("Perimeter formula: Height1+Height2+Breadth2")
        print("Perimeter of Triangle:", Height1+Height2+Breadth2)