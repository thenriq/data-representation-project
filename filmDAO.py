import mysql.connector
class FilmDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )
        
    
    def create(self, film):
        cursor = self.db.cursor()
        sql="insert into films (id,movie_name, movie_gender, movie_year, movie_box_office) values (NULL, %s,%s,%s,%s)"
        values = [
            #login['id'], --> for auto-increment table this will not be used
            film['movie_name'],
            film['movie_gender'],
            film['movie_year'],
            film['movie_box_office']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from films"
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
       sql="select * from films where id = %s"
       values = [id]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       return self.convertToDictionary(result)
    
    def convertToDictionary(self, result):
        colnames=['id','movie_name','movie_gender','movie_year','movie_box_office']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

filmDAO = FilmDAO()