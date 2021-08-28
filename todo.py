#!/usr/bin/env python3

import sys


def read_list():
    file = open('/todolist.txt', 'r')
    result = file.read()
    file.close()
    return result

def write_list(content):
    file = open('/todolist.txt', 'w')
    file.write(content)
    file.close()

def delete(item):
    content = read_list()
    cont_line = content.split('\n')
    is_exist = False
    for line in cont_line:
        if line:
            if item == line:
                cont_line.remove(item)
                is_exist = True
                break
    if not is_exist:
        print('no such task.')
        return
    content = ''
    for line in cont_line:
        if line:
            content += line + '\n'
    write_list(content)

def show():
    print(read_list())

def add_item(item):
    content = read_list()
    if item in content:
        print('task exist.')
    else:
        content += item + '\n'
        write_list(content)

def help_task():
    help_var = '''
        -h or --help                 ===> help
        -a or --add     [your task]  ===> add task
        -d or --delete  [your task]  ===> delete task
        -s or --show                 ===> show tasks
    '''
    print(help_var)

def main():
    if len(sys.argv) == 1:
        print('required argument.')
    else:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            help_task()
        elif sys.argv[1] == '-s' or sys.argv[1] == '--show':
            show()
        elif sys.argv[1]  == '-a' or sys.argv[1] == '--add':
            if len(sys.argv) == 3:
                add_item(sys.argv[2])
            else:
                print('invalid argument(s).')
        elif sys.argv[1]  == '-d' or sys.argv[1] == '--delete':
            if len(sys.argv) == 3:
                delete(sys.argv[2])
            else:
                print('invalid argument(s).')
        else:
            print('invalid argument(s).')

if __name__ == '__main__':
    main()
