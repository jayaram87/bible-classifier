import os
import yaml
from src.utils.log import Logger
import pandas as pd
import json
from zipfile import ZipFile

class common_ops:
    def read_yaml(self, path: str) -> dict:
        """
        Function to read yaml file and returns as a dictionary of the config file
        """
        try:
            with open(path) as file:
                content = yaml.safe_load(file)
            Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'yaml file: {path} has been loaded successfully')
            return content
        except Exception as e:
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'yaml file: {path} wasnt been loaded successfully \n')
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')

    def create_directories(self, paths: list) -> None:
        """
        Function creates directories from a list of names
        """
        try:
            for path in paths:
                os.makedirs(path, exist_ok=True)
            Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'{path} directory created')
        except Exception as e:
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{path} directory wasnt created \n')
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')

    def save_json(self, path: str, data: str) -> None:
        """
        Function saves the data in the given path
        """
        try:
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
            Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'json file {file} saved')
        except Exception as e:
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'json file {file} wasnt saved \n')
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')

    def unzip_file(self, source: str, dest: str) -> None:
        """
        Function unzips the source zip file into the destination path
        """
        try:
            Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'Unzipping started...........')
            with ZipFile(source, 'r') as file2:
                file2.extractall(dest)
            Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'extracted {source} to {dest}')
        except Exception as e:
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'Error when unzipping files from {source} to {dest} \n')
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')



    
