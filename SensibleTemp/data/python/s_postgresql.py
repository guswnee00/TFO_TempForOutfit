import psycopg2
import csv
import sys

host = 'arjuna.db.elephantsql.com'
user = 'silvzcal'
password = 'zgPVPdBzmASs7_c6luaOkl6c3sXZdz39'
database = 'silvzcal'

def main():
    # postgresql 연결
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        # 커서 생성
        cur = conn.cursor()
    except:
        sys.exit()

    # 만약 summer 테이블 있다면 삭제
    cur.execute("DROP TABLE IF EXISTS summer;")

    # 테이블 생성
    cur.execute("""CREATE TABLE summer(
        SDate DATE, 
        Temperature FLOAT,
        Humidity FLOAT,
        SensibleTemp FLOAT)
    """)

    # csv 파일 속 데이터 옮기기
    with open ('data/csv/summer.csv', 'r') as s_file :
        s_reader = csv.DictReader(s_file)
        for data in s_reader:
            cur.execute("INSERT INTO summer(SDate, Temperature, Humidity, SensibleTemp) VALUES (%s, %s, %s, %s)",
                        (data['Date'], data['Temperature'], data['Humidity'], data['SensibleTemp']))

    conn.commit()

if __name__=='__main__':
    main()
