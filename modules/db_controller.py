import pymysql
'''connect root, kmong_db'''


# 기본키가 있다면, update 없다면 insert 되는 쿼리문 작성
def update_data_query(xlsx_to_db_data_list):

    '''connect root, kmong_db'''
    conn = pymysql.connect(host='localhost', user='root', password ='root', db='kmong_db',port =3306, charset='utf8')

    def sql():
        
        sql = '''
        INSERT INTO test_table( '최신파일명', '쇼핑몰', '주문일', '온라인상품명', '옵션', '판매자관리코드',	'주문수량', '금액', '배송비', '주문자명', '수령자명', '주소' )
        VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
        ON DUPLICATE KEY UPDATE
            '쇼핑몰' = %s,
            '주문일' = %s, 
            '온라인상품명' = %s,
            '옵션' = %s,
            '판매자관리코드' = %s,
            '주문수량' = %s,
            '금액' = %s, 
            '배송비' = %s, 
            '주문자명' = %s, 
            '수령자명' = %s, 
            '주소' = %s, 
        '''
        return sql


    try:
        query = sql()
        with conn.cursor() as curs:
            for i in range(len(xlsx_to_db_data_list)):

                curs.execute(query, (xlsx_to_db_data_list[i][0], xlsx_to_db_data_list[i][1], xlsx_to_db_data_list[i][2], 
                                    xlsx_to_db_data_list[i][3], xlsx_to_db_data_list[i][4], xlsx_to_db_data_list[i][5], 
                                    xlsx_to_db_data_list[i][6],xlsx_to_db_data_list[i][7], xlsx_to_db_data_list[i][8],
                                    xlsx_to_db_data_list[i][9], xlsx_to_db_data_list[i][10], xlsx_to_db_data_list[i][11],
                
                                    xlsx_to_db_data_list[i][1], xlsx_to_db_data_list[i][2], xlsx_to_db_data_list[i][3], 
                                    xlsx_to_db_data_list[i][4], xlsx_to_db_data_list[i][5], xlsx_to_db_data_list[i][6],
                                    xlsx_to_db_data_list[i][7], xlsx_to_db_data_list[i][8], xlsx_to_db_data_list[i][9], 
                                    xlsx_to_db_data_list[i][10], xlsx_to_db_data_list[i][11]))
            
            conn.commit()
    finally:
        conn.close()

xlsx_to_db_data_list = [["1","2","3","4","5","6","7","8","9","10","11","12"]]
update_data_query(xlsx_to_db_data_list)