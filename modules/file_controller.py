import os

def Find_the_latest_files(root_dir, d_day):
    root_dir = "../매출분석/"
    max_year = ""
    max_month = ""

    # 위 코드에서 형태를 파악한 뒤 원하는 값 추출
    temp_cnt = 0
    for (root, dirs, files) in os.walk(root_dir):
        if temp_cnt == 0:
            max_year = max(dirs) # 년도 중에 제일 최고 값을 저장
            temp_cnt += 1
        elif temp_cnt == 1:
            max_month = max(dirs) # 월 중에서 제일 최고 값을 저장
            break


    # 젤 최신 폴더를 탐색 했으니 경로 재지정
    re_root_dir = root_dir + max_year + "/" + max_month + "/"


    # 이제 최신 d-day만큼의 파일 경로를 저장 후 값을 반환값
    return_list = []
    for (root, dirs, files) in os.walk(re_root_dir):
        try: # try, except문 : 폴더에 엑셀 파일의 갯수가 d-day값 보다 작으면 에러가 뜰 수 있기 떄문에 처리
            files.sort(reverse = True) # 최신순으로 해야되어서 역순으로 바꿔주었다.
            temp_list = [] # 임시로 저장해서
            
            for i in range(0, d_day):
                temp_list.append(re_root_dir + files[i]) # 한 업체의 경로 포함 파일 이름을 다 합쳐준 뒤 
            return_list.append(temp_list) # 저장
        
        except:
            continue # 에러 발생시 그냥 무시하고 계속 진행
    
    return return_list