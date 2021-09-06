import os

def Find_the_latest_files(root_dir, d_day):
    max_year = ""
    max_month = ""

    # 임시로 출력해보는 코드 (데이터 형태를 파악하기 위함)
    # for i in os.walk(root_dir):
    #     print(i)
    
    # 위 코드에서 형태를 파악한 뒤 원하는 값 추출
    # dirs가 비어있고, files가 가득차있으면 최 하단 경로인 것.
    temp_cnt = 0
    for (root, dirs, files) in os.walk(root_dir):
        if len(dirs) == 0 and len(files) > 0:
            temp_cnt += 1
            print(temp_cnt)
            print('-' * 30)
            print("root : ",  root)
            print('-' * 30)
            print("dirs : ", dirs)
            print('-' * 30)
            print("files : ", files)
            print('-' * 30)
        # if temp_cnt == 0:
        #     max_year = max(dirs) # 년도 중에 제일 최고 값을 저장
        #     temp_cnt += 1
        # elif temp_cnt == 1:
        #     max_month = max(dirs) # 월 중에서 제일 최고 값을 저장
        #     temp_cnt += 1
        #     break
        # 4월 동기화 안됨    

    # print(max_year)
    # print(max_month)

    

    # # 젤 최신 폴더를 탐색 했으니 경로 재지정
    # re_root_dir = root_dir + "/" + max_year + "/" + max_month
    # print(re_root_dir)

    # temp_cnt = 0
    # for (root, dirs, files) in os.walk(re_root_dir):
    #      if temp_cnt == 0:
    #          store_list = dirs
    #          break
    
    # print(store_list)

    # # 이제 최신 d-day만큼의 파일 경로를 저장 후 값을 반환값
    # return_list = []
    # j = 0
    # for (root, dirs, files) in os.walk(re_root_dir):
    #     try: # try, except문 : 폴더에 엑셀 파일의 갯수가 d-day값 보다 작으면 에러가 뜰 수 있기 떄문에 처리
    #         files.sort(reverse = True) # 최신순으로 해야되어서 역순으로 바꿔주었다.
    #         temp_list = [] # 임시로 저장해서
            
    #         for i in range(0, d_day):
    #             temp_list.append(re_root_dir + store_list[j] + "/" + files[i]) # 한 업체의 경로 포함 파일 이름을 다 합쳐준 뒤 
    #         return_list.append(temp_list) # 저장
    #         j+=1

    #     except:
    #         continue # 에러 발생시 그냥 무시하고 계속 진행
    
    # # 어떤 값을 반환해주는지 예시 출력
    # for i in range(len(return_list)):
    #     print(return_list[i])


# 테스트용 함수 호출 부분
# Find_the_latest_files(매출분석 파일 위치 or 년도별 상위 폴더 위치, d_day)
Find_the_latest_files("C:/Users/Han/Desktop/외주_log/크몽/xlsx_to_db/매출분석", 3)