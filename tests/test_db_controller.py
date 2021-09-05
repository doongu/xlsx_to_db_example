import pymysql
'''connect root, kmong_db'''
conn = pymysql.connect(host='localhost', user='root', password ='root', db='kmog_db',port =3306, charset='utf8')
curs = conn.cursor()



def create_table():
    global curs
    sql = '''CREATE TABLE test_table (
                최신파일명 varchar(255) NOT NULL PRIMARY KEY,
                쇼핑몰 varchar(255) NOT NULL,
                주문일 varchar(255) NOT NULL,
                온라인상품명 varchar(255) NOT NULL,
                옵션 varchar(255) NOT NULL,
                판매자관리코드 varchar(255) NOT NULL,
                주문수량 varchar(255) NOT NULL,
                금액 varchar(255) NOT NULL,
                배송비 varchar(255) NOT NULL,
                주문자명 varchar(255) NOT NULL,
                수령자명 varchar(255) NOT NULL,
                주소 varchar(255) NOT NULL
            )
    '''
    curs.execute(sql)

'''create, test'''
def test_create():
    global curs
    curs.execute("Insert into test_table(최신파일명, 쇼핑몰, 주문일, 온라인상품명, 옵션, 판매자관리코드, 주문수량, 금액, 배송비, 주문자명, 수령자명, 주소) VALUES('test', 'test', 'test', 'test', 'test', 'test','test','test','test','test','test','test')")
    print(" 데이터를 추가하였습니다 ! ")

'''select test'''
def test_select():
    global curs
    answer = curs.execute("select * from test_table")
    print(" 데이터를 조회하겠습니다 ! ")
    print(answer)

# '''update test'''
# def test_update():
#     global curs
#     curs.execute("update compTBL SET compID='hjk'")
#     print("데이터를 업데이트 하였습니다 ! ")

'''delete test'''
def test_delete():
    global curs
    curs.execute("Delete FROM test_table")
    print("데이터를 삭제하였습니다 ! ")


# test_create()
# test_select()
# test_update()
# test_delete()


# 커밋
conn.commit()