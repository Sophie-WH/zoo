import random
 
Min = 1
Max = 6
def main():
     again = 'y'
     
     while again == 'y' or again == 'Y':
         print("Rolling the dice...")
         print("Their values are:")
         print(random.randint(Min, Max))
         print(random.randint(Min, Max))
         
         again = input("Roll them again? (y = yes):")
main()