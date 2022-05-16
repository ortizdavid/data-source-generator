from src.value_generator import ValueGenerator as gen

class Context:

    fields = []
    data_types = []
    max_values = []
    min_values = []

    _allowed_formats = {'SQL', 'CSV', 'TXT', 'JSON'}
    _allowed_data_types = {'INT', 'STR', 'FLOAT', 'DATE', 'TIME', 'DATETIME'}
    

    def __init__(self, name, data_format, num_fields) -> None:
        self._name = name
        self._num_fields = num_fields
        self._data_format = data_format


    def add_field_prop(self, name, type, min, max):
        self.fields.append(name)
        self.data_types.append(type)
        self.min_values.append(min)
        self.max_values.append(max)
       

    def is_allowed_format(self):
        return self._data_format.upper() in self._allowed_formats


    def is_alowed_type(self, type):
        return type.upper() in self._allowed_formats


    def generate_field_value(self, type, min, max):
        if type.upper() == 'INT':
            return gen.generate_int(min, max)
        elif type.upper() == 'FLOAT': 
            return gen.generate_float(min, max)
        elif type.upper() == 'DATE': 
            return gen.generate_date(min, max)
        elif type.upper() == 'DATETIME': 
            return gen.generate_date_time(min, max)
        elif type.upper() == 'TIME': 
            return gen.generate_time(min, max)
        else:
            return None


    def generate_field_value_str(self, prefix, max):
        return gen.generate_str(prefix.upper(), max)


