import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)


import csv
from io import StringIO
from pathlib import Path
from pypdf import PdfReader
from agentos.rag.data import JsonData,TextData,PdfData,CsvData
   
   

def text_load(file_path,**kwargs):
    encoding = kwargs.get('encoding')
    with open(file_path, 'r' , encoding=encoding) as file:
        content = file.read()
        
    return TextData(content,encoding)

def json_load(file_path,**kwargs):
    encoding = kwargs.get('encoding')
    with open(file_path, 'r' , encoding=encoding) as file:
        content = file.read()
        
    return JsonData(content,encoding)

def pdf_load(file_path,**kwargs):  
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    #page = reader.pages[0]
    #text = page.extract_text()
    
    page_str=""
    for i in range(number_of_pages):
        page_str = page_str+reader.pages[i].extract_text()
         

    return PdfData(page_str,number_of_pages)

# def csv_load(file_path,**kwargs):
#     encoding = kwargs.get('encoding')
    
   
#     content=""
#     with open(file_path, 'r', encoding=encoding) as f:
#         reader = csv.reader(f)     
#         for row in reader:
#             content += ','.join(row)
#             content += '\n'

#     if content.endswith('\n'):
#         content = content[:-1]

#     return CsvData(content,encoding)


def csv_load(file_path, **kwargs):
    encoding = kwargs.get('encoding')
    
    content = ""
    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.reader(f)
        headers = []
        try:
            headers = next(reader)  # 读取标题行
        except StopIteration:
            pass  # 处理空文件
        
        content_buffer = StringIO()
        writer = csv.writer(content_buffer)
        
        for row in reader:
            # 生成属性:值对
            pairs = [f"{header}:{value}" for header, value in zip(headers, row)]
            writer.writerow(pairs)  # 使用csv.writer正确处理特殊字符
        
        content = content_buffer.getvalue()
        # 移除末尾的换行符
        if content.endswith('\n'):
            content = content[:-1]
    
    return CsvData(content, encoding)


load_fun_dict={
    ".txt":text_load,
    ".json":json_load,
    ".pdf":pdf_load,
    ".csv":csv_load
}
    

class DataLoader:
    def __init__(
        self,
        file_path:str,
        encoding:str = "utf-8", #for [text_load,json_load]
    ):
        self.file_path=file_path
        self.encoding=encoding
    
    def load_data(
        self
    ):
        file_suffix = Path(self.file_path).suffix
        data=load_fun_dict[file_suffix](
            file_path=self.file_path,
            encoding=self.encoding
        )
        return data  




# import sys
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(os.path.dirname(current_dir))
# sys.path.insert(0, project_root)

# import csv
# from pathlib import Path
# from pypdf import PdfReader
# from agentos.rag.data import JsonData,TextData,PdfData,CsvData
# from config.settings import Config

# def csv_load(file_path,**kwargs):
#     encoding = kwargs.get('encoding')   
#     content=""
#     with open(file_path, 'r', encoding=encoding) as f:
#         reader = csv.reader(f)     
#         for row in reader:
#             content += ','.join(row)
#             content += '\n'   
#     return CsvData(content,encoding)

# csv=csv_load(project_root+Config.DATA["csv"],encoding="utf-8")
# print(csv.content)
# print("=====================================")
# print(csv.get_content())
# print("=====================================")
# print(csv.get_metadata())