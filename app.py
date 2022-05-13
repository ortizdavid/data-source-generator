from src.context import Context
from src.json_src import JSONSrc
from src.csv_src import CSVSrc
from src.sql_src import SQLSrc
from src.txt_src import TxtSrc

print("1 - English [EN]\n2 - Portuguese [PT]")
language = input("Choose language: ")

if language in ['PT', 'pt', '1']:
    from lang.labels_pt import *
    from lang.messages_pt import *
if language in ['EN', 'en', '2']:
    from lang.labels_en import *
    from lang.messages_en import *

name = input(LBL_CONTEXT_NAME)
data_format = input(LBL_DATA_FORMAT) 
num_fields = int(input(LBL_NUMBER_OF_FIELDS))

# Context or Problem or Table
context = Context(name, data_format, num_fields)

#Creating fields and its values
for i in range(num_fields):
    
    field = input(f"{LBL_FIELD} {i+1}, {LBL_FIELD_NAME}")
    data_type = input(f"{LBL_FIELD} {i+1}, {LBL_FIELD_DATA_TYPE}")
    min = input(LBL_MIN_VALUE)
    max = input(LBL_MAX_VALUE)
    context.add_field_prop(field, data_type, min, max)

    if data_type.upper() not in context._allowed_data_types:
        print(f"'{data_type}'{MSG_ERR_NOT_ALLOWED_TYPE}")
        break

print(MSG_SUCESS_FIELDS_ADDED)
num_rows = int(input(LBL_NUMBER_OF_ROWS))
dir_src = "data-source/"

if data_format.upper() == 'SQL':
    sql = SQLSrc(context)
    sql.create_src(num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'CSV':
    csv = CSVSrc(context)
    csv.create_src(num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'TXT':
    txt = TxtSrc(context)
    txt.create_src(num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'JSON':
    json = JSONSrc(context)
    json.create_src(num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")
else:
    print(f"'{data_format}' {MSG_ERR_NOT_ALLOWED_FORMAT}")
