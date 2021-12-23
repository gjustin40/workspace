import os
import json

from tqdm import tqdm

def split_json(json_file, target_dir='result'):

    with open(json_file, 'r') as f:
        json_data = json.load(f)

        image_data_list = json_data['images']
        annotation_data_list = json_data['annotations']
        categories_data = json_data['categories']

        annotations_by_image_dict = {}
        for image_data in image_data_list:
            image_id = image_data['id']
            
            annotations_by_image_dict[image_id] = []

        for annotation_data in annotation_data_list:
            image_id = annotation_data['image_id']
            annotations_by_image_dict[image_id].append(annotation_data)

    json_dict = {}
    for image_data, annotations in tqdm(zip(image_data_list, annotations_by_image_dict.values())):
        image_filename = image_data['file_name']
        image_filename_ext = image_filename.split('.')[-1]

        json_filename = image_filename.replace(image_filename_ext, 'json')
        json_path = os.path.join(target_dir, json_filename)

        json_dict['images'] = image_data
        json_dict['categories'] = categories_data
        json_dict['annotations'] = annotations

        with open(json_path, 'w') as f:
            json.dump(json_dict, f)
    
    print(f'Finished Splitting! ({len(image_data)})')

    return None


if __name__ == '__main__':

    split_json('example.json')