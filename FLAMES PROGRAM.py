#flames program using python
def rel(con):
    while True:
         if con=='f':
             print("You both are Friends")
             break
         elif con=='l':
             print("You both are Lovers")
             break
         elif con=='a':
             print("You both are only affection,hahaha")
             break
         elif con=='m':
             print("You both are marraige very soon,congreats...")
             break
         elif con=='e':
             print("Your both are Enimeys,better luck next time")
             break
         elif con=='s':
             print("sorry that girl your  sister your life single only ")
             break
   
    
n1=input("Enter Boy name :")
n1=n1.lower()
n1.replace(" ","")
n1_list=list(n1)
#print(n1_list)

n2=input("Enter Girl name :")
n2=n2.lower()
n2.replace(" ","")
n2_list=list(n2)
#print(n2_list)


for i in n1_list[:]:
    if i in n2_list:
        n1_list.remove(i)
        n2_list.remove(i)
#print(n1_list)
#print(n2_list)
l=len(n1_list)+len(n2_list)
#print(len())
#print(l)


con='flames'
i=0
while len(con)>1:
    v=(l%len(con))-1
    if v>= 0:
        con = con[v + 1:] + con[:v]
    else: 
         con = con[:len(con) - 1]
#print(con[0])
rel(con)

    

    


   
    
    
    
    
    
        
