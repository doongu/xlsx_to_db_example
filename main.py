from modules import file_controller, xlsx_controller

file_location_list = file_controller.Find_the_latest_files("../매출분석/", 3)
# print(file_location_list)
xlsx_to_db_data_list= xlsx_controller.data_selecter(file_location_list)
# print(xlsx_to_db_data_list)
for i in range(len(xlsx_to_db_data_list)):
    print(xlsx_to_db_data_list[i])
# db_controller.update_data_query(xlsx_to_db_data_list)