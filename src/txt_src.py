from src.context import Context
from src.file_src import FileSrc as fs

class TxtSrc:


    def __init__(self, context: Context):
        self._context = context


    def get_txt_values(self):
        
        ctx = self._context
        end_value = "\t"
        counter = 0
        str_values = "" 
        values = []
        
        for i in range(0, ctx._num_fields):
            if ctx.data_types[i].upper() == 'STR':
                values.append(ctx.generate_field_value_str(ctx.fields[i], ctx.max_values[i]))
            else:
                values.append(ctx.generate_field_value(ctx.data_types[i], ctx.min_values[i], ctx.max_values[i]))
        
        for value in values:
            counter += 1
            if counter == len(ctx.fields):  end_value = ""
            str_values += f'{value}{end_value}'

        return f"{str_values}\n"


    def get_txt_fields(self):
        
        ctx = self._context
        counter = 0
        end_field = "\t"
        str_fields = ""
        
        for field in ctx.fields:
            counter += 1
            if counter == len(ctx.fields): end_field = ""
            str_fields += f'{field}{end_field}' 
    
        return f'{str_fields}\n'


    def create_src(self, num_rows: int, dir: str):
        ctx = self._context
        fname = fs.create_name(ctx._name)
        txt = self.get_txt_fields()
        for i in range(num_rows):
            txt += self.get_txt_values()
        fs.write_file(dir + fname +'.'+ ctx._data_format, txt)    


