import shelve
import sys

DIR = sys.argv[1]
database_name = sys.argv[2]
question_list = sys.argv[3]
code_name = sys.argv[4]
key = sys.argv[5]
OS_type=sys.argv[6]

if "linux-gnu" == OS_type:
    ql = shelve.open(f'/{DIR}/Databases/{database_name}.db')
else:
    ql = shelve.open(f'/{DIR}/Databases/{database_name}')

try:
    master_list = ql[f'{question_list}']
    total=len(master_list)
    for index in range(0, total):
        question_dict=master_list[index]
        if question_dict.get("Code Name") == code_name:
            print(question_dict.get(key))
            break
        index+=1
except:
    print("Question does not appear.")
finally:
    ql.close()
