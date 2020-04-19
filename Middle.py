import sys
import pymysql
import datetime

#creating a connection
dbServerName    = "localhost"
dbUser          = "root"
dbPassword      = "elitecheer"
dbName          = "cs4400spring2020"
charSet         = "utf8mb4"

con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName, charset=charSet)

# Login_01 line 31
# Returns True or False
def authenticateUser(username, password):
    return True

    with con as cursor:
        query = 'SELECT username, password FROM user WHERE username = %s and password = md5(%s)'
        cursor.execute(query, (username, password))
        if cursor.fetchall() != () or cursor.fetchall() is not None:
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
            query = "CALL register(%s, %s, %s, %s, %s, %s, %s);"
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

#ManageBuildingStationWindow_04
# YOU CAN ONLY DELETE BUILDINGS THAT YOU JUST CREATED WITH NO MENU ITEMS
    # DO NOT TRY TO DELETE REAL BUILDINGS
def removeBuilding(building) :
    with con as cursor :
        cursor.execute('call ad_delete_building(%s);', (building))
        con.commit()

#ManageBuildingStationWindow_04
        # YOU CAN ONLY DELETE STATIONS YOU JUST CREATED
def removeStation(bldgName) :
    with con as cursor :
        cursor.execute('select stationname from station where buildingName = %s', (bldgName))
        data = cursor.fetchall()
        if(len(data)>=1) :
            cursor.execute('call ad_delete_station(%s)', (data[0][0]))
        con.commit()

# CreateBuilding_05 line
# Inserts building into database. Tags is an array of tags
def insertBuilding(building, description, tags):
    with con as cursor :
        cursor.execute('call ad_create_building(%s, %s);', (building, description))
        for tag in tags :
            cursor.execute('call ad_add_building_tag(%s, %s)', (building, tag))
        con.commit()

#CreateBuilding_05, UpdateBuilding_06
def addTag(building, tag) :
    with con as cursor :
        cursor.execute('call ad_add_building_tag(%s, %s);', (building, tag))
        con.commit()

#CreateBuilding_05, UpdateBuilding_06
def removeTag(building, tag) :
    with con as cursor :
        cursor.execute('call ad_remove_building_tag(%s, %s);', (building, tag))
        con.commit()

#UpdateBuilding_06, CreateBuilding_05
def getTags(building) :
    with con as cursor :
        cursor.execute('call ad_view_building_tags(%s);', (building))
        cursor.execute('select * from ad_view_building_tags_result')
        data = cursor.fetchall()
        return [data[i][0] for i in range(0, len(data))]

#UpdateBuilding_06, gets the deets
def viewBuilding(building) :
    with con as cursor :
        cursor.execute('call ad_view_building_general(%s);', (building))
        cursor.execute('select * from ad_view_building_general_result')
        data = cursor.fetchall()
        return [data[0][0], data[0][1]]


# UpdateBuilding_06
#should be able to change the name
def updateBuilding(ogbuilding, building, description):
        with con as cursor :
            cursor.execute('call ad_update_building(%s, %s, %s);', (ogbuilding, building, description))
            con.commit()

# CreateStation_07
def insertStation(station, capacity, sponsoredBuilding):
    with con as cursor :
        cursor.execute('call ad_get_available_building()',)
        cursor.execute('call ad_create_station(%s, %s, %s)', (station, sponsoredBuilding, capacity))
        con.commit()

# CreateStation_07
def getAvailableBuilding() :
    with con as cursor :
        cursor.execute('call ad_get_available_building()',)
        cursor.execute('select * from ad_get_available_building_result',)
        data = cursor.fetchall()
        return [i[0] for i in data]

# UpdateStation_08
def viewStation(bldgName) :
    with con as cursor :
        cursor.execute('select stationname from station where buildingName = %s', (bldgName))
        data = cursor.fetchall()
        if(len(data)>=1) :
            cursor.execute('call ad_view_station(%s)', (data[0][0]))
            cursor.execute('select * from ad_view_station_result',)
            data = cursor.fetchall()
            return [data[0][0], data[0][1], data[0][2]]
        return None

# UpdateStation_08
def updateStation(station, capacity, sponsoredBuilding):
    with con as cursor:
        cursor.execute('call ad_update_station(%s, %s, %s)', (station, capacity, sponsoredBuilding))
        con.commit()



# ManageFood_09
# sortedBy in ('name', 'menucount', 'purchasecount')
# sorteddirection in ('ASC', 'DESC')
# Returns list of tuples. Tuples are in format (foodName, MenuCount, PurchaseCount)

def manageFoodFilter(foodName, sortedBy, sortedDirection):
    if sortedBy == None :
        sortedBy = 'name'
        
    with con as cursor :
        query = 'call ad_filter_food(%s, %s, %s);'
        cursor.execute(query, (foodName, sortedBy, sortedDirection))
        cursor.execute('select * from ad_filter_food_result',)
        data = cursor.fetchall()
        result = [(data[i][0], data[i][1], data[i][2]) for i in range(0, len(data))]
    return result


# ManageFood_09
# Removes the food from the database
def deleteFood(foodName):
    with con as cursor:
        query = 'CALL ad_delete_food(%s)'
        cursor.execute(query, foodName)
        con.commit()

    return True

# CreateFood_10
# Inserts the new food into the database
def insertFood(foodName):
    with con as cursor:
        query = 'CALL ad_create_food(%s)'
        cursor.execute(query, foodName)
        con.commit()

    return True

# Screen 14 Manager Food Truck Summary - Ben IK you haven't done this one yet but im ahead of u
# dates should be valid dates (python datetime.date), or they will be turned to None
# sorted by should be (None, 'foodTruckName', 'totalOrder', 'totalRevenue', 'totalCustomer')
# sortedDirection should be (None, ASC, DESC)
def foodTruckSummaryFilter(username, foodTruckName, stationName, dateMin, dateMax, sortedBy, sortedDirection) :
    result = []

    #useful info for later
    # we can create dates to pass to mysql using datetime.date(year, month, day) out of integers
    #until this is implemented ill just pass None jajaja
    if (not isinstance(dateMin, datetime.date)) :
        dateMin = None

    if (not isinstance(dateMax, datetime.date)) :
        dateMax = None

    with con as cursor :
        query = 'call mn_filter_summary(%s, %s, %s, %s, %s, %s, %s);'
        cursor.execute(query, (username, foodTruckName, stationName, dateMin, dateMax, sortedBy, sortedDirection))
        cursor.execute('select * from mn_filter_summary_result',)
        data = cursor.fetchall()
        result = [(data[i][0], data[i][1], data[i][2], data[i][3]) for i in range(0, len(data))]
    return result


# ManageFoodTruck_11
# Reuturns list of tuples. Tuples are in format (truckName, stationName, remainingCpaacity, staff, # Menu Item)
# staffMin and staffmax better fecking be numbers
# and has capacity better be a booleeen
def manageFoodTruckFilter(username, truckName, stationName, staffMin, staffMax, hasCapacity):

    with con as cursor :
        query = 'call mn_filter_foodtruck(%s, %s, %s, %s, %s, %s);'
        cursor.execute(query, (username, truckName, stationName, staffMin, staffMax, hasCapacity))
        cursor.execute('select * from mn_filter_foodtruck_result',)
        data = cursor.fetchall()
        result = [(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]) for i in range(0, len(data))]
    return result #demo [("FT 1", "Station 1", 4, 3, 10), ("FT 2", "Station 2", 5, 7, 20)]

# CreateFoodTruck_12
# returns staff of manager
def getStaff(manager):
    return ["Staff 1", "Staff 2,", "Staff 3"]

# Explore_16 line 13
# Returns list of all building names
def getBuildingNames():

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
    with con as cursor:
        query = 'CALL cus_select_location(%s,%s);'
        cursor.execute(query, (username, station))
        con.commit()

    return True

# Explore_16 line 55
# Returns list of tuples (rows) which fulfill criteria
def exploreFilter(buildingName, stationName, buildingTag, truckName, food):
    givenArgs = (buildingName, stationName, buildingTag, truckName, food)
    for arg in givenArgs:
        if arg == '':
            arg = None

    with con as cursor:
        query = ('CALL cus_filter_explore(%s, %s, %s, %s, %s);')
        cursor.execute(query, (givenArgs[0],givenArgs[1],givenArgs[2],givenArgs[3],givenArgs[4]))
        con.commit()
        query = 'SELECT * FROM cus_filter_explore_result;'
        cursor.execute(query)
        data= cursor.fetchall()
        # deal with null values
        data = [['' if j is None else j for j in i] for i in data]
        # reformat
        result = [(data[i][0], data[i][1], data[i][2].split(','), data[i][3].split(',')) for i in range(0, len(data))]

        return result

# CurrentInformation_17 line 13
# Returns tuple(station name, building name, )
def getCurrentInformation(username):
    with con as cursor:
        query = ('call cus_current_information_basic(%s);')
        cursor.execute(query, (username))
        con.commit()
        data= cursor.fetchall()
        # deal with null values
        data = [['' if j is None else j for j in i] for i in data]
        # reformat
        result = [data[0][0], data[0][1], data[0][2].split(','), data[0][3], data[0][4]]

    return result
    # ("Station One", "Building One", ["ADA", "Chemistry"], "Description here", 100)

# CurrentInformation_17 line 21
# Returns list of tuples. Each tuple is one row --> tuple(Food truck, Manager, list(foods))
def getTrucksAtStation(username):
    with con as cursor:
        query = ('call cus_current_information_foodtruck(%s);')
        cursor.execute(query, (username))
        con.commit()
        data= cursor.fetchall()
        # deal with null values
        data = [['' if j is None else j for j in i] for i in data]
        # reformat
        result = [(data[i][0], data[i][1], data[i][2].split(',')) for i in range(0, len(data))]

    return result
    #[("Food Truck One", "Manager One", ["Apple", "Banana"]), ("Food Truck Two", "Manager Two", ["Orange", "Grape"])]

# Order_18
# Gets truck menu all (food, price)
def getTruckMenu(truckName):
    return [("Apple", 3), ("Banana", 5)]

# Order_18
# Purchases is list of tuple(foodName, quantity) and date is date
def submitOrder(purchases, date):
    pass

# TODO
# OrderHistory_19 line ??
# Returns list of tuples. Each tuple is one row --> tuple(Date, orderID, orderTotal, Food(s), food quantity)
def getOrderHistory(username):
    with con as cursor:
        query = ('call cus_order_history(%s);')
        cursor.execute(query, (username))
        con.commit()
        data = cursor.fetchall()
        # deal with null values
        data = [['' if j is None else j for j in i] for i in data]
        # reformat
        result = [(data[i][0], data[i][1], data[i][2], data[i][3].split(','), data[i][2]) for i in range(0, len(data))]

    return result
    # return [("2020-01-20", "000001", 14, ["Apple, Banana"], 5), ("1999-01-25", "000002", 17, ["Chocolate, Chips"], 10)]
