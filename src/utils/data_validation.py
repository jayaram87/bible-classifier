import os
import yaml
from src.utils.log import Logger
import pandas as pd
import json

class DataValidation:
    def dframe(self, file):
        """
        function returns a pandas dataframe
        """
        try:
            with open(os.path.join(os.getcwd(), 'data', 'avila', 'avila-description.txt')) as descfile:
                details = descfile.readlines()[25:37]
            col_df = pd.DataFrame(details)
            return col_df

        except Exception as e:
            pass


    def dtype_validation(self, file_path: str, file_type:str):
        """
        function validates the data type of all the rows in the training and test files
        """
        try:
            if file_type == 'train':
                with open(file_path) as tfile:
                    content = yaml.safe_load(tfile)
                Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'yaml file: {file_path} has been read successfully')

        except Exception as e:
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'yaml file: {file_path} wasnt validated successfully \n')
            Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')