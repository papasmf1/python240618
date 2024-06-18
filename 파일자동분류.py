import os
import shutil

# 경로 설정
download_folder = r'C:\Users\user\Downloads'
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 파일 이동 함수
def move_files(extension_list, destination_folder):
    for file_name in os.listdir(download_folder):
        if any(file_name.lower().endswith(ext) for ext in extension_list):
            source_path = os.path.join(download_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(source_path, destination_path)
            print(f'Moved: {source_path} to {destination_path}')

# 확장자에 따라 파일 이동
move_files(['.jpg', '.jpeg'], image_folder)
move_files(['.csv', '.xlsx'], data_folder)
move_files(['.txt', '.doc', '.pdf'], docs_folder)
move_files(['.zip'], archive_folder)
