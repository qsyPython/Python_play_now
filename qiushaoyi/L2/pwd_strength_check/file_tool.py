
class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        with open(self.filepath,'a',newline='') as f:
            f.write(line)

    def read_from_file(self):
        with open(self.filepath,'r',newline='') as f:
            lines = f.readlines()
            return lines

