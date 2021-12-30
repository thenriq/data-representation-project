import mysql.connector
class LogProfileDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )
    
            
    def create(self, login):
        cursor = self.db.cursor()
        sql="insert into loginprofile (id,username, password, email) values (NULL, %s,%s,%s)"
        values = [
            #login['id'], --> for auto-increment table this will not be used
            login['username'],
            login['password'],
            login['email']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select id, username, email from loginprofile"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDictionary(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select id, username, email from loginprofile where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, profile):
        cursor = self.db.cursor()
        sql="update loginprofile set username= %s, password=%s, email=%s  where id = %s"
        values = [
            profile['username'],
            profile['password'],
            profile['email'],
            profile['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return profile
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from loginprofile where id = %s"
        values = [id]
        cursor.execute(sql, values)

        return {}

    def convertToDictionary(self, result):
        colnames=['id','username','email']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
logprofileDAO = LogProfileDAO()