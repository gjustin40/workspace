import shutil
import os
import glob
import xml.etree.ElementTree as ET


def rejection_dir(xml_list, defalut_path):
    # dir path 값 설정
    xml_path = f'{defalut_path}/Annotations'
    jpg_path = f'{defalut_path}/JPEGImages'
    for xml in xml_list:
        # xml 파싱
        xml_data = ET.parse(xml)
        root = xml_data.getroot()

        # rejection_check tag 찾기
        rejection_check = root.find('rejection_check')

        # rejection_check tag.text  == False 면
        false = 'False'
        f = xml.split('.')[-2]
        fl = f.split('\\')[1]
        xml_file = f'{xml_path}/{fl}.xml'
        jpg_file = f'{jpg_path}/{fl}.jpg'

        if rejection_check is None:
            _trash_dir = f'{defalut_path}/trash'
            if not os.path.isdir(_trash_dir):
                os.makedirs(_trash_dir)

            if not os.path.isdir(f'{_trash_dir}/JPEGImages'):
                os.makedirs(f'{_trash_dir}/JPEGImages')

            if not os.path.isdir(f'{_trash_dir}/Annotations'):
                os.makedirs(f'{_trash_dir}/Annotations')

            print(xml_file)
            shutil.move(jpg_file, f'{_trash_dir}/JPEGImages')
            shutil.move(xml_file, f'{_trash_dir}/Annotations')

        elif rejection_check.text == false:
            # rejection 폴더 안에 trash 폴더 만들어 이둉
            _trash_dir = f'{defalut_path}/trash'
            if not os.path.isdir(_trash_dir):
                os.makedirs(_trash_dir)

            if not os.path.isdir(f'{_trash_dir}/JPEGImages'):
                os.makedirs(f'{_trash_dir}/JPEGImages')

            if not os.path.isdir(f'{_trash_dir}/Annotations'):
                os.makedirs(f'{_trash_dir}/Annotations')
                
            print(xml_file)
            shutil.move(jpg_file, f'{_trash_dir}/JPEGImages')
            shutil.move(xml_file, f'{_trash_dir}/Annotations')

            # 삭제 기능
            # print(xml_file)
            # os.remove(xml_file)
            # os.remove(jpg_file)


def main():
    TEST_DIR = True
    worker_list = ['A', 'C', 'D', 'E', 'I']

    # 나중 워커 설정해서 자동적으로
    for i in worker_list:

        defalut_path = f'S:/traffic_night2/{i}/rejections'
        xml_list = glob.glob(f'{defalut_path}/Annotations/*.xml')
        if xml_list is None:
            pass
        else:
            # print(xml_list)
            rejection_dir(xml_list,defalut_path)

    # 한 작업자씩 수동적으로
    # defalut_path = 'S:/traffic_night/E/rejections'
    # xml_list = glob.glob(f'{defalut_path}/Annotations/*.xml')
    # # print(xml_list)
    # rejection_dir(xml_list, defalut_path)


if __name__ == "__main__":
    main()
