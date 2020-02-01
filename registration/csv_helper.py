import chardet


def get_file_encoding(file_path):
    '''
    获取文件编码
    '''
    encoding = None
    binary_data = None
    with open(file_path, 'rb') as bf:
        binary_data = bf.read()
    if isinstance(binary_data, bytes):
        detected = chardet.detect(binary_data)
        encoding = isinstance(detected, dict) and detected.get('encoding', None)
    return encoding

if __name__ == '__main__':
    print(get_file_encoding(__file__))
