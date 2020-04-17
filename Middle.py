import pymysql

#creating a connection
dbServerName    = "localhost"
dbUser          = "root"
dbPassword      = "gojackets"
dbName          = "cs4400spring2020"
charSet         = "utf8mb4"

con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName, charset=charSet)

# Login_01 line 31
# Returns True or False
def authenticateUser(username, password):
    with con as cursor:
        query = 'SELECT username, password FROM user WHERE username = %s and password = md5(%s)'
        cursor.execute(query, (username, password))
        if cursor.fetchall != ():
            return True

    return False

# Register_02 line ??
# Return True if able to add user, False otherwise
def insertUser(username, password, email, firstname, lastname, balance, userType):
    with con as cursor:
            query = "CALL register(%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (username, email, firstname, lastname, password, balance, userType))
            con.commit()

    return True

# Home_03 line 22
# Returns the type of user (admin, employee, staff)
def getUserType(username):
    return "admin" # Placeholder

    admin = []
    employee = []
    staff = []

    with con as cursor:
        query = "SELECT COUNT(username) FROM admin WHERE username = %s"
        cursor.execute(query, (username))
        admin = cursor.fetchall()[0][0]

        query = "SELECT COUNT(username) FROM employee WHERE username = %s"
        cursor.execute(query, (username))
        emloyee = cursor.fetchall()[0][0]

        query = "SELECT COUNT(username) FROM staff WHERE username = %s"
        cursor.execute(query, (username))
        staff = cursor.fetchall()[0][0]

    if admin == 1:
        return "admin"
    elif employee == 1:
        return "employee"
    else:
        return "staff"

# ManageBuildingStationWindow_04 line ??
# Returns list of tuples fulfilling criteria
def manageBuildingStationFilter(building, BuildingTag, stationName, capacityMin, capacityMax):
    return [("Building One", ["ADA", "Chemistry"], "Station One", "4", ["Food Truck One", "FT2"]), ("Building Two", ["ADA", "Chemistry"], "Station One", "4", ["Food Truck One", "FT2"])]

# Explore_16 line 13
# Returns list of all building names
def getBuildingNames():

    with con as cursor:
        query = "select distinct(buildingName) from building;"
        cursor.execute(query)
        nested_list = cursor.fetchall()

    buildings = []
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
        result = []
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
