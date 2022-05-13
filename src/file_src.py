import os
import time

class FileSrc:

    def write_file(file_name, content):
        if os.path.isfile(file_name):
            os.remove(file_name)
        else:
            file = open(file_name, "a")
            file.write(content)
            file.close()

    def create_name(prefix):
        return f'{prefix}-{time.strftime("%Y%m%d-%H%M%S")}'


