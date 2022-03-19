import os
import sys


b = [120, 160, 208]
output_file = 'list_output.txt'


'''
                                            output in fotmat as ['a','b','c']
'''
def write_single_array_into_text(arr, dest):
    with open(os.path.join(os.path.dirname(sys.argv[0]), dest), 'w', encoding='UTF-8') as f:
        index = 0
        arr_length = len(arr)
        f.write('[')
        for num in arr:
            f.write(str(num))
            if index is not (arr_length - 1):
                f.write(',')
            index += 1
        f.write(']')


if __name__ == '__main__':
    write_single_array_into_text(b, output_file)
