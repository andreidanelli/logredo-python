# Adaptador de banco de dados PostgreSQL
import psycopg2
# Load data from metadata
import UploadMetadados


# Connect to the Bank and run the script
def connectionDatabase(sql):
    connection = psycopg2.connect(host='localhost', database='logredo', user='root', password='root');
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as Error:
        print("Database Error: %s" % Error)
        connection.rollback()
        cursor.close()
        return 1
        
    cursor.close()

# Commands DML Database
def commandSelectAll():
    sql = 'SELECT * FROM t_logredo ORDER BY ID'
    return connectionDatabase(sql)

def commandInsert(ID, A, B):
    sql = f'INSERT INTO t_logredo VALUES ({ID}, {A}, {B})'
    return connectionDatabase(sql)

def commandUpdate(ID, FIELD, VALUE):
    sql = f'UPDATE t_logredo SET {FIELD}={VALUE} WHERE ID = {ID}'
    return connectionDatabase(sql)

def commandCreateTable():
    sql = 'CREATE TABLE t_logredo (ID INTEGER PRIMARY KEY, A INTEGER NULL, B INTEGER NULL)'
    return connectionDatabase(sql)

def commandDropTable():
    sql = 'DROP TABLE IF EXISTS t_logredo'
    return connectionDatabase(sql)

# Load metadata files for table
def archiveToTable():
    try:
        output = UploadMetadados.uploadMetadados()

        for line in output:
            commandInsert(line[0], line[1], line[2])
    except:
        print('Error loading data for insert command!')

# Commands executed in table
def load():
    try:
        commandDropTable()   # If exists table drop
        commandCreateTable() # Create table
        archiveToTable()     # Load metadata files for table
    except:
        print('Error when executing DML commands!');