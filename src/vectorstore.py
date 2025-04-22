import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)



from agentos.rag.data import merge_content
from agentos.rag.load import DataLoader, csv_load, pdf_load
from config.settings import Config
from agentos.rag.split import CharacterSplit, RowSplit
from agentos.rag.embedding import EmbeddingModel
from agentos.rag.store import ChromaDB
from chromadb.api import ClientAPI
from chromadb.api.models.Collection import Collection



def process_data():

    # 加载数据
    csv=DataLoader(project_root+Config.DATA["csv"],encoding="utf-8").load_data()
    pdf=DataLoader(project_root+Config.DATA["pdf"],encoding="utf-8").load_data()

    # 拆分数据
    csv_split=RowSplit(chunk_row_size=1,chunk_overlap=0).split(csv)
    pdf_split=RowSplit(chunk_row_size=1,chunk_overlap=0).split(pdf)

    # 嵌入模型
    embedding=EmbeddingModel(
        model_name="BAAI/bge-base-zh-v1.5",
        cache_dir="/mnt/7T/xz"
    )

    #存储数据
    vector_db1=ChromaDB.create_document(
        embedding_model=embedding,
        if_persist=True,
        dir=project_root+Config.VECTORSTORE1_PATH
    )
    vector_db1.add_data(csv_split)
    vector_db2=ChromaDB.create_document(
        embedding_model=embedding,
        if_persist=True,
        dir=project_root+Config.VECTORSTORE2_PATH
    )
    vector_db2.add_data(pdf_split)

    return vector_db1,vector_db2


if __name__ == "__main__":
    process_data()





# csv=csv_load(project_root+Config.DATA["csv"],encoding="utf-8")
# csv=DataLoader(project_root+Config.DATA["csv"],encoding="utf-8").load_data()
# print("====================csv.content====================")
# print(csv.get_content())
# print("====================csv.metadata===================")
# print(csv.get_metadata())

# pdf=pdf_load(project_root+Config.DATA["pdf"],encoding="utf-8")
# pdf=DataLoader(project_root+Config.DATA["pdf"],encoding="utf-8").load_data()
# print("====================pdf.content====================")
# print(pdf.get_content())
# print("====================pdf.metadata===================")
# print(pdf.get_metadata())



# csv_split=RowSplit(chunk_row_size=1,chunk_overlap=0).split(csv)
# print("====================csv_split====================")
# for c in csv_split:
#     print(c.get_content())
# print(csv_split[0].get_content())
# pdf_split=RowSplit(chunk_row_size=1,chunk_overlap=0).split(pdf)
# print("====================pdf_split====================")
# for p in pdf_split:
#     print(p.get_content())
# print(pdf_split[0].get_content())



# csv_content=merge_content(csv_split)
# print("====================csv_documents====================")
# print(csv_content)
# pdf_content=merge_content(pdf_split)
# print("====================pdf_documents====================")
# print(pdf_content)



# embedding=EmbeddingModel(
#     model_name="BAAI/bge-base-zh-v1.5",
#     cache_dir="/mnt/7T/xz"
# )
# vector_db1=ChromaDB.create_document(
#     embedding_model=embedding,
#     if_persist=True,
#     dir=project_root+Config.VECTORSTORE1_PATH
# )
# vector_db1.add_data(csv_split)
# vector_db2=ChromaDB.create_document(
#     embedding_model=embedding,
#     if_persist=True,
#     dir=project_root+Config.VECTORSTORE2_PATH
# )
# vector_db2.add_data(pdf_split)




# vector_db1=ChromaDB.load_document(
#     embedding_model=embedding,
#     dir=project_root+Config.VECTORSTORE1_PATH
# )
# vector_db2=ChromaDB.load_document(
#     embedding_model=embedding,
#     dir=project_root+Config.VECTORSTORE2_PATH
# )
# docs1=vector_db1.query_data("高血压",query_num=5,rerank=False)
# docs2=vector_db2.query_data("高血压",query_num=5,rerank=False)
# print("====================csv_documents====================")
# for d in docs1:
#     print(d.get_content())
# print("====================pdf_documents====================")
# for d in docs2:
#     print(d.get_content())
