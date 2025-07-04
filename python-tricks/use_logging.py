import os
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
logging_file = os.path.join(script_dir, 'test.log')

print(f'Save log in {logging_file}')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)

logging.debug('Start program')
logging.info('Some actions')
logging.info('End program')
