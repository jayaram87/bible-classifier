import argparse
import os
from src.utils.common import common_ops
from src.utils.log import Logger
import urllib.request as req

stage = 'GET DATA'

def main(config_path):
    """
    Function to download and extract zip file from ucl repo using ML Ops workflow
    """
    config = common_ops.read_yaml(config_path)
    url = config['data']['source_url']
    local_dir = config['data']['local_dir']

    common_ops.create_directories([local_dir])

    data_file = config['data']['data_file']
    data_file_path = os.path.join(local_dir, data_file)

    print(data_file_path)

    if not os.path.isfile(data_file_path):
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'Downloading file.....')
        with req.urlopen(url) as file:
            with open(data_file_path, 'wb') as file1:
                file1.write(file.read())
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'filename {data_file} created ')
    else:
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'file {data_file} already downloaded')

    unzip_data_dir = config['data']['unzip_data_dir']
    if not os.path.exists(unzip_data_dir):
        common_ops().create_directories(['unzip_data_dir'])
        common_ops().unzip_file(source=data_file_path, dest=unzip_data_dir)
    else:
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'file {data_file} already extracted')
    

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', '-c', default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'\n********************')
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'stage {stage} started')
        main(config_path=parsed_args.config)
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'stage {stage} completed')
    except Exception as e:
        Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'stage {stage} incomplet')
        Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)} /n')
        raise e
