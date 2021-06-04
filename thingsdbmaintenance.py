import sqlite3
# setup data
class thingsdbmaintenance :
    
    def createThingsTable (self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("CREATE TABLE mythings (thing_ID  int, thingname text, category text, actor text);")
        conn.close()
    def createCatsTable (self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("CREATE TABLE mycats (catname text);")
        conn.close()
    def createActorsTable (self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("CREATE TABLE myactors (actorname text);")
        conn.close()
    
    def deleteThings(self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("delete from mythings" )  
        conn.commit()
        conn.close()
    def deleteCats(self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("delete from mycats" )  
        conn.commit()
        conn.close()
    def deleteActors(self ):
        conn = sqlite3.connect('thingsFantastics.db')
        conn.execute("delete from myactors" )  
        conn.commit()
        conn.close()
        
        
    def insertThingsTable (self , thingname, cat, act):
        conn = sqlite3.connect('thingsFantastics.db')
        inserts = "insert into mythings ( thing_ID, thingname, category, actor) " 
        valuest = " values (3, ?, ?, ?) "
        query = inserts + valuest 
        conn.execute(query, (thingname, cat, act,)) 
        conn.commit()
        conn.close()
        
    def insertCatsTable (self , name):
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute("select *  from mycats   where catname like ? order by catname ", (name,))
        mybool = False
        for line in mydata:   # is the category there
            # code
            mybool= True
        if not mybool :       # # if the category is not there, asdd it
            inserts = "insert into mycats (catname) "
            valuest   = "values (? ) "
            query = inserts + valuest    
            conn.execute(query, (name,) ) 
            conn.commit()
            print("Category added to database: ", name)
        conn.close()
        
    def insertActorsTable (self , name):
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute("select *  from myactors   where actorname like ? order by actorname ", (name,))
        mybool = False
        for line in mydata:  # is the actor there?
            # code
            mybool= True
        if not mybool :      # if the actor is not there, add him/her
            inserts = "insert into myactors (actorname) " 
            valuest   = "values ( ? ) "
            query = inserts + valuest       
            conn.execute(query, (name,) ) 
            conn.commit() 
            print("Actor added to database: ", name)
        conn.close()
        
    def showThingsAll (self ):
        selects = "select * "
        froms   = "from mythings  "
        where = " "     
        orderby = "order by thingname "
        query = selects + froms +  where +  orderby 
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query) 
        print ( "All Things: ")
        for line in mydata:
            # code
            print(line)
        conn.close()
  
    def showThingSome (self , name ) :
        selects = "select * "
        froms   = "from mythings  "
        where = " where thingname like ? "     
        orderby = "order by thingname "
        query = selects + froms +  where +  orderby 
        name = '%'+name+'%'
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query, (name,) )
        print ( "Things found like ", name , ":")
        for line in mydata:
            # code
            print (line)
        conn.close()
      
    def showCatsAll(self ):
        selects = "select * "
        froms   = "from mycats "
        orderby = "order by catname "
        where = " "     
        query = selects + froms +  where +  orderby 
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query) 
        print ( "All Cats: ")
        for line in mydata:
            # code
            print(line)
        conn.close()
        
    def showActorsAll(self ):
        selects = "select * "
        froms   = "from myactors "
        where = " "  
        orderby = "order by actorname " 
        query = selects + froms +  where +  orderby 
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query) 
        print ( "All Actors: ")
        for line in mydata:
            # code
            print(line)
        conn.close()
    
        
    def findThingAdd (self , name, cat, act,):
        selects = "select * "
        froms   = "from mythings  "
        where = " where thingname like ? "     
        orderby = "order by thingname "
        query = selects + froms +  where +  orderby 
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query, (name,) )
#        print ( "Things found: ")
        mybool = False
        for line in mydata:
            # code
            mybool= True
        if not mybool :
            inserts = "insert into mythings ( thing_ID, thingname, category, actor) " 
            valuest = " values (3, ?, ?, ?) "
            query = inserts + valuest 
            conn.execute(query, (name, cat, act,)) 
            conn.commit()
            print("Movie added to database: ", name)
        conn.close()
 
    def showCatSome (self , name ) :  # show all movies in the category
        selects = "select * "
        froms   = "from mythings  "
        where = " where category like ? "     
        orderby = "order by category, thingname "
        query = selects + froms +  where +  orderby 
        name = '%'+name+'%'
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query, (name,) )
        print ( "Categories found like ", name , ":")
        for line in mydata:
            # code
            print (line)
        conn.close()
    
    def showActSome (self , name ) :  # show all movies with this actor
        selects = "select * "
        froms   = "from mythings  "
        where = " where actor like ? "     
        orderby = "order by actor, thingname "
        query = selects + froms +  where +  orderby 
        name = '%'+name+'%'
        conn = sqlite3.connect('thingsFantastics.db')
        mydata = conn.execute(query, (name,) )
        print ( "Actors found like ", name , ":")
        for line in mydata:
            # code
            print (line)
        conn.close()
    