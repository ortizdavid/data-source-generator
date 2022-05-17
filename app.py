from src.context import Context
from src.data_src_caller import DataSrcCaller


print("1 - English [EN]\n2 - Portuguese [PT]")
language = input("Choose language: ")

if language in ['EN', 'en', '1']:
    from lang.labels_en import *
    from lang.messages_en import *
elif language in ['PT', 'pt', '2']:
    from lang.labels_pt import *
    from lang.messages_pt import *
else:
    print("Incorrect Language!")

print()
name = input(LBL_CONTEXT_NAME)
data_format = input(LBL_DATA_FORMAT) 
num_fields = int(input(LBL_NUMBER_OF_FIELDS))

# Context or Problem or Table
context = Context(name, data_format, num_fields)

print()
#Creating fields and its values
for i in range(num_fields):
    
    field = input(f"{LBL_FIELD} {i+1}, {LBL_FIELD_NAME}")
    data_type = input(f"{LBL_FIELD} {i+1}, {LBL_FIELD_DATA_TYPE}")
    min = input(LBL_MIN_VALUE)
    max = input(LBL_MAX_VALUE)
    context.add_field_prop(field, data_type, min, max)

    if  data_type.upper() not in context._allowed_data_types:
        print(f"'{data_type}' {MSG_ERR_NOT_ALLOWED_TYPE}")
        break

print()
print(MSG_SUCESS_FIELDS_ADDED)
num_rows = int(input(LBL_NUMBER_OF_ROWS))
#dir_src = input("Directory for Data Source: ")
dir_src = "data-source/"

if data_format.upper() == 'SQL':
    DataSrcCaller.call_sql_src(context, num_rows, dir_src) 
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'CSV':
    DataSrcCaller.call_csv_src(context, num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'TXT':
    DataSrcCaller.call_txt_src(context, num_rows, dir_src)
    print(f"'{data_format}'- {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'JSON':
    DataSrcCaller.call_json_src(context, num_rows, dir_src)
    print(f"'{data_format}' {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() == 'XML':
    DataSrcCaller.call_xml_src(context, num_rows, dir_src)
    print(f"'{data_format}' {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

elif data_format.upper() in ['ALL', 'A', 'TODOS', 'T']:
    DataSrcCaller.call_all_src(context, num_rows, dir_src) 
    print(f"'{data_format}' {MSG_SUCESS_SOURCE_GREATED} {MSG_SUCESS_DIRECTORY} '{dir_src}'")

else:
    print(f"'{data_format}' {MSG_ERR_NOT_ALLOWED_FORMAT}")
