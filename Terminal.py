import argparse
from Matrix import Matrix
from Modify import modify_data
import logging

logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} function "{funcName}()" line {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Action between two matrix")
    parser.add_argument('-m_1', type=list, action='append', default=
    [['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2', type=list, action='append', default=
    [['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-operation', type=str, default='*')

    args = parser.parse_args()

    m_1 = modify_data(args.m_1)
    m_2 = modify_data(args.m_2)

    if args.operation == '+':
        print(f'Summ: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif args.operation == '*':
        print(f'Multiply>: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'Equation: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Operation {args.operation} cannot be done')
        logger.info(f'Operation {args.operation} cannot be done')