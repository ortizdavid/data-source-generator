from src.context import Context
from src.file_src import FileSrc as fs

class XMLSrc:
    
    def __init__(self, context: Context):
        self._context = context

    def create_xml(self):
        ctx = self._context
        str_fields = "" 
        values = []
    
        for i in range(0, ctx._num_fields):
            if ctx.data_types[i].upper() == 'STR':
                values.append(ctx.generate_field_value_str(ctx.fields[i], ctx.max_values[i]))
            else:
                values.append(ctx.generate_field_value(ctx.data_types[i], ctx.min_values[i], ctx.max_values[i]))

        str_fields +=  f'\t<{ctx._name}>\n'
        for i in range(0, ctx._num_fields):
            str_fields += f'\t\t<{ctx.fields[i]}>{values[i]}</{ctx.fields[i]}>\n'
        str_fields += f'\t</{ctx._name}>\n'
        return  str_fields


    def create_src(self, num_rows: int, dir: str):
        ctx = self._context
        fname = fs.create_name(ctx._name)
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<root>\n'
        for i in range(num_rows):
            xml += self.create_xml()
        xml += '</root>'
        fs.write_file(dir + fname +'.'+ ctx._data_format, xml)   
