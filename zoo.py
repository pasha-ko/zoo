import pickle

class Zoo:
    def __init__(self,name):
        self.text=name
        
def count(zoo):
    if hasattr(zoo,"yes"):       
       return count(zoo.yes)+count(zoo.no) 
    else: return 1

def ask(q):
    
    while True:
        try:
            answer = input(q+"? \n").upper()
            if answer[0] == 'Y':
                return True
            elif answer[0] == 'N':
                return False
        except:
            pass

def guess(zoo):
    if hasattr(zoo,"yes"):       
        if ask(zoo.text):
            guess(zoo.yes)
        else:
            guess(zoo.no)
    else:
        print ("I guess your animal is",zoo.text)
        if ask("Right"):
            print('yay I found it! :)')
        else:
        
            
            animal = input("what is your animal? \n")
            question = input ("what is the differense between " + animal + " and " + zoo.text+"? \n")

            zoo.yes = Zoo(animal)
 
            zoo.no = Zoo(zoo.text)

            zoo.text = question
            
try:
    file=open('zoo','rb')
    zoo = pickle.load(file)
    file.close()
except:
    zoo=Zoo("zebra")

while True:
    print("Hello! Think of an animal in english")
    print("Всего ",count(zoo), "животных")
    guess(zoo)
    file=open('zoo','wb')
    pickle.dump(zoo,file)
    file.close()
