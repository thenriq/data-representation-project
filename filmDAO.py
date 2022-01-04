import mysql.connector
import dbconfig as cfg
class FilmDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
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
   
    def update(self, films):
         cursor = self.db.cursor()
         sql="update films set movie_name= %s, movie_gender=%s, movie_year=%s, movie_box_office=%s  where id = %s"
         values = [
             films['movie_name'],
             films['movie_gender'],
             films['movie_year'],
             films['movie_box_office'],
             films['id']
         ]
         cursor.execute(sql, values)
         self.db.commit()
         return films
     
    def delete(self, id):
       cursor = self.db.cursor()
       sql="delete from films where id = %s"
       values = [id]
       cursor.execute(sql, values)

       return {}
    
    def convertToDictionary(self, result):
        colnames=['id','movie_name','movie_gender','movie_year','movie_box_office']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

filmDAO = FilmDAO()