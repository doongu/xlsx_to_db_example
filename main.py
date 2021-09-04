from modules import file_controller, xlsx_controller, db_controller

file_location_list = file_controller.Find_the_latest_files("../매출분석/", 2)
xlsx_to_db_data_list= xlsx_controller.data_selecter(return_list)
db_controller.update_data_query(xlsx_to_db_data_list)