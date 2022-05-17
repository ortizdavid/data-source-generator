from src.context import Context
from src.json_src import JSONSrc
from src.csv_src import CSVSrc
from src.sql_src import SQLSrc
from src.txt_src import TxtSrc
from src.xml_src import XMLSrc

class DataSrcCaller:
    

    @classmethod
    def call_sql_src(cls, context: Context, num_rows: int, dir_src: str):
        sql = SQLSrc(context)
        sql.create_src(num_rows, dir_src) 


    @classmethod
    def call_csv_src(cls, context: Context, num_rows: int, dir_src: str):
        csv = CSVSrc(context)
        csv.create_src(num_rows, dir_src)


    @classmethod
    def call_txt_src(cls, context: Context, num_rows: int, dir_src: str):
        txt = TxtSrc(context)
        txt.create_src(num_rows, dir_src)  


    @classmethod
    def call_json_src(cls, context: Context, num_rows: int, dir_src: str):
        json = JSONSrc(context)
        json.create_src(num_rows, dir_src) 

    @classmethod
    def call_xml_src(cls, context: Context, num_rows: int, dir_src: str):
        json = XMLSrc(context)
        json.create_src(num_rows, dir_src)  


    @classmethod
    def call_all_src(cls, context: Context, num_rows: int, dir_src: str):
        if context._data_format.upper() in ['ALL', 'A', 'TODOS', 'T']:
            context._data_format = 'SQL'
            cls.call_sql_src(context, num_rows, dir_src)
            context._data_format = 'CSV'
            cls.call_csv_src(context, num_rows, dir_src)
            context._data_format = 'TXT'
            cls.call_txt_src(context, num_rows, dir_src)
            context._data_format = 'JSON'
            cls.call_json_src(context, num_rows, dir_src)
            context._data_format = 'XML'
            cls.call_xml_src(context, num_rows, dir_src)

