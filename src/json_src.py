from src.context import Context
from src.file_src import FileSrc as fs

class JSONSrc:

    def __init__(self, context: Context):
        self._context = context

    def create_json(self):
        
        ctx = self._context
        str_fields = str_value = "" 
        end = ", "
        values = []
        counter = 0
    
        for i in range(0, ctx._num_fields):
            if ctx.data_types[i].upper() == 'STR':
                values.append(ctx.generate_field_value_str(ctx.fields[i], ctx.max_values[i]))
            else:
                values.append(ctx.generate_field_value(ctx.data_types[i], ctx.min_values[i], ctx.max_values[i]))

        str_fields +=  '\t{'
        for i in range(0, ctx._num_fields):
            counter += 1
            if counter == ctx._num_fields: end = ''
            str_value = values[i] if isinstance(values[i], int) or isinstance(values[i], float) else f'"{values[i]}"'
            str_fields += f'"{ctx.fields[i]}": {str_value}{end}'
        str_fields += '}' 
        return  str_fields


    def create_src(self, num_rows: int, dir: str):
        ctx = self._context
        fname = fs.create_name(ctx._name)
        json = "[\n"
        end = ',\n'
        counter = 0
        for i in range(num_rows):
            counter += 1
            if counter == num_rows: end = ''
            json += self.create_json() + end
        json += "\n]"
        fs.write_file(dir + fname +'.'+ ctx._data_format, json)    


