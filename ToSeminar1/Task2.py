# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

print('x  y  z  ¬(X ⋁ Y ⋁ Z)   ¬X ⋀ ¬Y ⋀ ¬Z')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
           print(f'{x}  {y}  {z}        {~ (x | y | z)}           {~ x & ~ y & ~ z }')
           
    
                
