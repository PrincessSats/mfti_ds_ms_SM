import yadisk
import pandas as pd

yadisk_token = ''

def trasfer_to_yadisk():
    # Создаем объект Yadisk
    y = yadisk.YaDisk(token=yadisk_token)

    # Проверяем, доступен ли диск
    if not y.check_token():
        print("Token is not valid")
        return
    else:
        print("Token is valid")

    try:
        y.upload(xlsx_file_path, disk_file_path)
        print(f"File {xlsx_file_path} uploaded to Yadisk at {disk_file_path}")
    except Exception as e:
        print(f"Error uploading file: {e}")
        

def convert_csv_to_xlsx(csv_path, xlsx_path):
    df = pd.read_csv(csv_path)
    df.to_excel(xlsx_path, index=False)
    
if __name__ == "__main__":
    # Путь к локальному файлу CSV
    local_file_path = "/Users/mmms/Developer/user_log.csv"
    
    # Путь к файлу на Яндекс.Диске
    disk_file_path = "/user_log(1).xlsx"
    
    # Преобразуем CSV в XLSX
    xlsx_file_path = "/Users/mmms/Developer/user_log.xlsx"
    convert_csv_to_xlsx(local_file_path, xlsx_file_path)
    
    # Загружаем файл на Яндекс.Диск
    trasfer_to_yadisk()