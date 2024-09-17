import os
import sys
from src.exception import CustomException
from src.logger import logging
import yaml
import json
import joblib
import shutil
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import random
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomException(e, sys)

    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
def copy_random_imgfiles(src_dir, dest_dir, num_img):

    '''
    The titles of image files are 8 digit numbers between 00000000 and 00004999
    '''

    try:
        for folder in os.listdir(src_dir):

            # Create list of random number 
            random_int_list = unique_random_int_generator(min=0, max=4999, num_data=num_img)
            # Create list of random image file name
            random_str_list = ["0000" + "%04d" % integer + ".jpg" for integer in random_int_list]
            logging.info(f"{num_img} random image files are selected")

            dest_folder = os.path.join(dest_dir, folder)
            if not os.path.exists(dest_folder):

                os.makedirs(dest_folder)
                logging.info(f"New image folder is created. Folder directory: {dest_folder}")

            for filename in random_str_list:
            # Create full file path
                file_path = os.path.join(src_dir, folder, filename)
                file_path = Path(file_path)
                
                # Define the destination file path
                dest_path = os.path.join(dest_dir, folder, filename)
                # Copy the file
                shutil.copy(file_path, dest_path)
            logging.info(f"random images are copied and pasted into: {dest_dir}/{folder}")

    except Exception as e:
        raise CustomException(e, sys)



@ensure_annotations
def unique_random_int_generator(min:int, max:int, num_data:int):
    
    return random.sample(range(min, max+1), num_data)

# if __name__ == "__main__":
    
#     copy_random_imgfiles(src_dir="Bottle Images", dest_dir="raw_img", num_img=500)