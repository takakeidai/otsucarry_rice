

#mysql-connectorではなく、mysql-connector-pythonをinstall
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    # MYSQLのサーバーのパスワードを入力
    password = "mysqlのパスワード",
    port = "3306",
    auth_plugin='mysql_native_password',
    #mysqlでcreate database dictionary;によりデータベース生成後 database = 'dictionary'でデータベースを指定する
    database = 'dictionary'
)

mycursor = db.cursor()

if __name__ == '__main__':
    
    # wordsテーブル作成
    create_table_query = 'create table words (id integer primary key auto_increment, word varchar(255) not null);' 
    mycursor.execute(create_table_query)

    # データ挿入
    mycursor.execute("START TRANSACTION;")
    mycursor.execute("INSERT INTO words VALUES (1, 'かれーらいす');")
    mycursor.execute("INSERT INTO words VALUES (2, 'かれる');")
    mycursor.execute("INSERT INTO words VALUES (3, 'かれは');")
    mycursor.execute("INSERT INTO words VALUES (4, 'かれーこ');")
    mycursor.execute("INSERT INTO words VALUES (5, 'かれい');")
    mycursor.execute("INSERT INTO words VALUES (6, 'さみしさ');")
    mycursor.execute("INSERT INTO words VALUES (7, 'さいこう');")
    mycursor.execute("INSERT INTO words VALUES (8, 'さいたま');")
    mycursor.execute("INSERT INTO words VALUES (9, 'れいんこーと');")
    mycursor.execute("INSERT INTO words VALUES (10,'れしぴ');")
    mycursor.execute("INSERT INTO words VALUES (11,'れっとうかん');")
    mycursor.execute("INSERT INTO words VALUES (12,'れんしゅう');")
    mycursor.execute("INSERT INTO words VALUES (13,'れきし');")
    mycursor.execute("INSERT INTO words VALUES (14,'れんらく');")
    mycursor.execute("COMMIT;")
    
    # end of line break