import os


def write_to_txt(txt_path, to_write):
    '''
    Opens selected .txt file
    Writes row to selected .txt file
    '''
    with open(f'{os.getcwd()}\\ComposteraReviewed\\{txt_path}_reviewed.txt','a+') as f:
        f.write(str(to_write))
        f.write('\n')


