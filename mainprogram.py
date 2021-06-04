from exchild import exchild       # import the class

class mainprogram (exchild):   # create main program as a class
    
    obj = exchild ()           # create object  ( copy the functions into memory to make it available at runtime )
                                # obj refers to exchild, exchild imports ex1 , so obj can use all what is in ex1 as wells as what is in exchild
    
    obj.function1()        # saved in ex1  , welcome message
    
    
    #Use  all functions
    a = int ( input ('How many adults? '))
    day = input ('On which day would you like to see a movie?')
    if day == 'mon' :
        print ( "no movie on mondays")
    else: 
        sTP = obj.calcTicket(day)
    
        aCost = obj.calcA ( a, sTP )  # the the total amount for adults
        
        aCost = obj.discount(a, aCost)
        
        print ('ticket Price: ', sTP )  

        print ('totalTicketPrice is: ',  aCost)
    
    

        
    
    
# how many people are going the movies
# which day do they want to go
# if tue,wed,thur then sTP =10
# if fri  and sat then 20
# if sun the 30
# mon 0