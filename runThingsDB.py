from thingsdbmaintenance import thingsdbmaintenance

class rundb ( thingsdbmaintenance):
    obj = thingsdbmaintenance()
    
    try: 
        obj.createThingsTable ( )
    except:
        pass
    try: 
        obj.createCatsTable ( )
    except:
        pass
    try: 
        obj.createActorsTable ( )
    except:
        pass
#
#    obj.deleteThings()
#    obj.deleteCats()
#    obj.deleteActors()
    
    thingname = 'there is something about mary'
    catname = 'romance'
    actorname = 'julia' 
    obj.findThingAdd(thingname, catname, actorname) # if the movie is NOT there,  add it to the db
    obj.insertCatsTable( catname ) # if the category is NOT there,  add it to the db
    obj.insertActorsTable( actorname) # if the actor is NOT there,  add him/her to the db
    
    obj.showThingSome('mary')  # do I have this movie?
    obj.showActSome('lia')
    obj.showCatSome('fantasy')
    
    obj.showThingsAll()
    obj.showCatsAll()
    obj.showActorsAll()