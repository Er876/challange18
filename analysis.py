import json
import pandas as pd

def analysis(file, user_id):
    '''�� file json �ļ���ͳ�Ƴ� user_id ָ���û���ѧϰ����
    Args:
        file(str): json file name
        user_id(int): user id
    '''

    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0

    s = df[df['user_id'] == user_id].minutes
    return s.count(), s.sum()

def analysis_raw(file, user_id):
    '''�� file json �ļ���ͳ�Ƴ� user_id ָ���û���ѧϰ����
    Args:
        file(str): json file name
        user_id(int): user id
    '''

    times = 0
    minutes = 0

    try:
        f = open(file)
        records = json.load(f)
        for item in records:
            if item['user_id'] != user_id:
                continue
            times += 1
            minutes += item['minutes']
        f.close()
    except:
        pass
    return times, minutes
