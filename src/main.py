import mlflow
import os
from src.utils.common import common_ops
from src.utils.log import Logger

stage = 'main'
root = os.path.dirname(os.path.abspath(__file__))
os.environ['MLFLOW_TMP_DIR'] = root

common_ops.create_directories(['logs'])

def main():
    Logger(os.path.join('logs', 'logs.log')).logger('INFO', 'MLFLow process started')
    with mlflow.start_run() as run:
        mlflow.run('.', 'get_data', use_conda=False)

if __name__ == '__main__':
    try:
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', '\n********************')
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'stage {stage} started')
        main()
        Logger(os.path.join('logs', 'logs.log')).logger('INFO', f'stage {stage} completed')
    except Exception as e:
        Logger(os.path.join('logs', 'logs.log')).logger('ERROR', f'{str(e)}')
        raise e


