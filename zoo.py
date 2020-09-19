import pickle

class Zoo:
    def __init__(self,name):
        self.text=name

def guess(zoo):
    if hasattr(zoo,"yes"):       
        answer = input(zoo.text+"? \n")
        if answer[0] in ["y","Y"] :
            guess(zoo.yes)
        else:
            guess(zoo.no)
    else:
        print ("I guess your animal is",zoo.text)
        answer = input("Right? \n")
        if answer[0] in ["y","Y"] :
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
    guess(zoo)
    file=open('zoo','wb')
    pickle.dump(zoo,file)
    file.close()
