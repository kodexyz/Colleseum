import psycopg2
dbpassword='password'
try:
    conn = psycopg2.connect("dbname = 'players' user='jesus' host='localhost'")
except:
    print("failed")

print(dir(conn))