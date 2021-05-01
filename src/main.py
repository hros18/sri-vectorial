import sys

if __name__ == '__main__':
    if sys.argv.len < 4:
        print('Missing arguments')
        print('main.py <documents_path> <query_path> <rel_path>')
        return
    documents_path = sys.argv[1]
    query_path = sys.argv[2]
    rel_path = sys.argv[3]

    #todo process files
