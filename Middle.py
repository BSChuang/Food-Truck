import pymysql

#creating a connection
dbServerName    = "localhost"
dbUser          = "root"
dbPassword      = "password"
dbName          = "cs4400spring2020"
charSet         = "utf8mb4"

#con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName, charset=charSet)

# Login_01 line 31
# Returns True or False
def authenticateUser(username, password):
    return True # placeholder

    with con as cursor:
        query = 'SELECT username, password FROM user WHERE username = %s and password = md5(%s)'
        cursor.execute(query, (username, password))
        if cursor.fetchall != ():
            return True

    return False

# Register_02 line ??
# userType must be '', 'admin', 'manager', 'staff' otherwise sql will shit its pants
# Return True if able to add user, False otherwise (this is impossible/difficult bc no feedback from server procedure)
def insertUser(username, password, email, firstname, lastname, balance, userType):
    with con as cursor:
            #cant pass null to sql, as long as no email is given they won't be added to admin table
            if userType == None or userType == '' :
                userType = 'Admin'
            query = "CALL register(%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (username, email, firstname, lastname, password, balance, userType))
            con.commit()

    return True 

# Home_03 line 22
# Returns a list of types that the user belongs to, or an empty list if they are not found
def getUserType(username):
    return 'manager'
    result = []
    with con as cursor:
        query = "SELECT COUNT(username) FROM admin WHERE username = %s"
        cursor.execute(query, (username))
        if cursor.fetchall()[0][0] > 0:
            result.append( 'admin')

        query = "SELECT COUNT(username) FROM manager WHERE username = %s"
        cursor.execute(query, (username))
        if cursor.fetchall()[0][0] > 0 :
            result.append('manager')

        query = "SELECT COUNT(username) FROM staff WHERE username = %s"
        cursor.execute(query, (username))
        if cursor.fetchall()[0][0] > 0 :
            result.append('staff')
        
        query = "SELECT COUNT(username) FROM customer WHERE username = %s"
        cursor.execute(query, (username))
        if cursor.fetchall()[0][0] > 0 :
            result.append('customer')
        
    return result

# ManageBuildingStationWindow_04 line 89
# Returns list of tuples fulfilling criteria, use None or empty str if field is blank
# if we want different values to come back to replace nulls in the database, change value on line labeled 'deal with nulls'
def manageBuildingStationFilter(building, buildingTag, stationName, capacityMin, capacityMax):
    result = []
    with con as cursor :
        query = 'call ad_filter_building_station(%s, %s, %s, %s, %s);'
        cursor.execute(query, (building, buildingTag, stationName, capacityMin, capacityMax))
        cursor.execute('select * from ad_filter_building_station_result',)
        data = cursor.fetchall()
        # deal with null values
        data = [['' if j is None else j for j in i] for i in data]
        # reformat
        result = [(data[i][0], data[i][1].split(','), data[i][2], data[i][3], data[i][4].split(',')) for i in range(0, len(data))]
    return result
    #demo format
    #[("Building One", ["ADA", "Chemistry"], "Station One", "4", ["Food Truck One", "FT2"]), ("Building Two", ["ADA", "Chemistry"], "Station One", "4", ["Food Truck One", "FT2"])]

# CreateBuilding_05 line 
# Inserts building into database. Tags is an array of tags
def insertBuilding(building, description, tags):
    print(building, description, tags)
    pass

# UpdateBuilding_06
def updateBuilding(building, description, tags):
    print(building, description, tags)
    pass

# CreateStation_07
def insertStation(station, capacity, sponsoredBuilding):
    print(station, capacity, sponsoredBuilding)
    pass

# UpdateStation_08
def updateStation(station, capacity, sponsoredBuilding):
    print(station, capacity, sponsoredBuilding)
    pass

# ManaageFood_09
# Returns list of food names
def getFoods():
    return ["Apple", "Banana", "Chocolate"]

# ManageFood_09
# Returns list of tuples. Tuples are in format (foodName, MenuCount, PurchaseCount)
def manageFoodFilter(foodName):
    if foodName == None: # Return list of all foods
        return [("Apple", 10, 20), ("Banana", 1, 2)]
    else: # Return only that food
        return [("Banana", 1, 2)]

# ManageFood_09
# Removes the food from the database
def deleteFood(foodName):
    print(foodName)
    pass

# CreateFood_10
# Inserts the new food into the database
def insertFood(foodName):
    print(foodName)
    pass

# ManageFoodTruck_11
# Reuturns list of tuples. Tuples are in format (truckName, stationName, remainingCpaacity, staff, # Menu Item)
def manageFoodTruckFilter(truckName, stationName, staffMin, staffMax, hasCapacity):
    return [("FT 1", "Station 1", 4, 3, 10), ("FT 2", "Station 2", 5, 7, 20)]

# CreateFoodTruck_12
# returns staff of manager
def getStaff(manager):
    return ["Staff 1", "Staff 2,", "Staff 3"]

# Explore_16 line 13
# Returns list of all building names
def getBuildingNames():
    return ['a', 'b', 'c']

    with con as cursor:
        query = "select distinct(buildingName) from building;"
        cursor.execute(query)
        nested_list = cursor.fetchall()

    buildings = [''] # we need an empty string at the beginning so the drop down boxes can start empty
    for li in nested_list:
        buildings.append(li[0])

    return buildings

# Explore_16 line 17
# Returns list of all station names
def getStationNames():
    return ['d', 'e', 'f']

    result = []
    with con as cursor :
        query = 'select distinct(stationName) from station'
        cursor.execute(query)
        result = [''] # we need an empty string at the beginning so the drop down boxes can start empty
        for i in cursor.fetchall():
            result.append(tuple(i)[0])

    return result

# Explore_16 line 66
# Sets the user's station location
def setUserStation(username, station):
    pass

# Explore_16 line 55
# Returns list of tuples (rows) which fulfill criteria
def exploreFilter(buildingName, stationName, buildingTag, truckName, food):
    givenArgs = (buildingName, stationName, buildingTag, truckName, food)
    for arg in givenArgs:
        if arg == '':
            arg = None

    print(givenArgs)

    with con as cursor:
        query = ('CALL cus_filter_explore(%s, %s, %s, %s, %s);')
        cursor.execute(query, (givenArgs[0],givenArgs[1],givenArgs[2],givenArgs[3],givenArgs[4]))
        con.commit()
        query = 'SELECT * FROM cus_filter_explore_result;'
        cursor.execute(query)
        print(list(cursor.fetchall()))
        return list(cursor.fetchall())

# CurrentInformation_17 line 13
# Returns tuple(station name, building name, )
def getCurrentInformation(username):
    return ("Station One", "Building One", ["ADA", "Chemistry"], "Description here", 100)

# CurrentInformation_17 line 21
# Returns list of tuples. Each tuple is one row --> tuple(Food truck, Manager, list(foods))
def getTrucksAtStation(station):
    return [("Food Truck One", "Manager One", ["Apple", "Banana"]), ("Food Truck Two", "Manager Two", ["Orange", "Grape"])]

# OrderHistory_19 line ??
# Returns list of tuples. Each tuple is one row --> tuple(Date, orderID, orderTotal, Food(s), food quantity)
def getOrderHistory(username):
    return [("2020-01-20", "000001", 14, ["Apple, Banana"], 5), ("1999-01-25", "000002", 17, ["Chocolate, Chips"], 10)]
