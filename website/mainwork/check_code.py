from . import config
import os
def check_dangerous_code(solution_id, language):
    realpath = os.path.join(config.work_dir, str(solution_id))
    filename = {
        'python3': "main.py",
        'g++': "main.cpp",
        'gcc':"main.c",
    }
    realpath = os.path.join(realpath, filename[str(language)])
    if language in ['python2', 'python3']:
        code=open(realpath,'r').readlines()
        support_modules = [
            're',  # ������ʽ
            'sys',  # sys.stdin
            'string',  # �ַ�������
            'scanf',  # ��ʽ������
            'math',  # ��ѧ��
            'cmath',  # ������ѧ��
            'decimal',  # ��ѧ�⣬������
            'numbers',  # �������
            'fractions',  # ������
            'random',  # �����
            'itertools',  # ��������
            'functools',
            #Higher order functions and operations on callable objects
            'operator',  # ��������
            'readline',  # ���ļ�
            'json',  # ����json
            'array',  # ����
            'sets',  # ����
            'queue',  # ����
            'types',  # �ж�����
        ]
        for line in code:
            if line.find('import') >= 0:
                words = line.split()
                tag = 0
                for w in words:
                    if w in support_modules:
                        tag = 1
                        break
                if tag == 0:
                    return False
        return True
    if language in ['gcc', 'g++']:
        code = open(realpath, 'r').read()
        if code.find('system')!=-1:
            return False
        return True

