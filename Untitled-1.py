def car():
    print("what car you prefer to drive")
    print("1:manual")
    print("2:auto")
    car = input("which one?")
    if(car=='1'):
        print("C")
    elif(car=='2'):
        print("java")

print("1:easy way " )
print("2:harder way " )
print("3:best way " )
print("4:hardest way")
platform = input("which platform?: ")

if(platform=='1'):
    print("python")
elif(platform=='2'):
    car()
elif(platform=='3'):
    print("python")
elif(platform=='4'):
    print("C++")
else:
    print("invalid option")    


def no():

    print("1:lego")
    print("2:play-doh")
    print("3:old-ugly")
    no=input("which one?")
    if(no=='1'):
        print("python")
    elif(no=='2'):
        print("ruby")    
    elif(no=='3'):
        print("pHp")    

def trysomenew():
    print("do you like to try something new?")
    print("1:yes")    
    print("2:no")
    platform = input("which one?: ")

if (platform=='1'):
    print("javascript")
elif(platform=='2'):
    no()

trysomenew()
