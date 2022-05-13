from src.context import Context
from src.file_src import FileSrc as fs

class SQLSrc:


    def __init__(self, context: Context):
        self._context = context


    def create_sql(self):
        
        ctx = self._context
        end_field = end_value = ", "
        counter = counter2 = 0
        str_fields = str_values = "" 
        values = []
        sql = f"INSERT INTO {ctx._name}"
        
        for field in ctx.fields:
            counter += 1
            if counter == len(ctx.fields): end_field = ""
            str_fields += f'{field}{end_field}' 
        sql += f'({str_fields}) VALUES '
        
        for i in range(0, ctx._num_fields):
            if ctx.data_types[i].upper() == 'STR':
                values.append(ctx.generate_field_value_str(ctx.fields[i], ctx.max_values[i]))
            else:
                values.append(ctx.generate_field_value(ctx.data_types[i], ctx.min_values[i], ctx.max_values[i]))
        
        for value in values:
            counter2 += 1
            if counter2 == len(ctx.fields): end_value = ""
            new_value = value if isinstance(value, int) or isinstance(value, float) else f'"{value}"'
            str_values += f'{new_value}{end_value}'
        sql += f"({str_values});\n"

        return sql


    def create_src(self, num_rows: int, dir: str):
        ctx = self._context
        fname = fs.create_name(ctx._name)
        sql = ""
        for i in range(num_rows):
            sql += self.create_sql()
        fs.write_file(dir + fname +'.'+ ctx._data_format, sql)    


