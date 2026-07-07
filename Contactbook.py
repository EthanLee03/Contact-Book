contacts = {
      "Ginger": "5942834854",
      "Brenda" : "2373732735",
      "Isaiah" : "2334334367",
    }


def main():
    
    question = (int(input("Would you like to (1) look someone up or (2) add a contact? ")))
    if question == 1:
        result = Lookup(contacts)
        print(result)
    if question == 2:
         result = Add(contacts)
         print("Contact Sucessfully added.")
    if question != 1 and question != 2: 
         print("That service is currently unavailable. Please Try again.")
         

def Lookup(contacts):
    name = (input("Who are you looking for? "))
    
    if name in contacts:
        return(contacts[name])
    else:
        return "That name is not currently in your contacts. Please try again or add a new contact."
    
    
def Add(contacts): 
    new_name = (input("Who are you adding to your contacts? "))

    new_number = (input("What is their 10 didget phone number? "))

    contacts[new_name] = new_number

        



main()
 
