#tool1 根据用户id在向量库查询历史体检信息
#tool2 根据用户病史和症状在向量库查询相似病人体检信息
#tool3 根据用户病史和症状在向量库查询疾病相关信息
#tool4 根据用户病史和症状使用浏览器查询疾病相关信息
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from agentos.rag.embedding import EmbeddingModel
from agentos.rag.store import ChromaDB
from config.settings import Config
from agentos.rag.data import merge_content

# embedding=EmbeddingModel(
#         model_name="BAAI/bge-base-zh-v1.5",
#         cache_dir="/mnt/7T/xz"
# )

embedding=EmbeddingModel(
        model_name="BAAI/bge-base-zh-v1.5",
        # cache_dir="/mnt/7T/xz"
)

v1=ChromaDB.load_document(
    embedding_model=embedding,
    dir=project_root+Config.VECTORSTORE1_PATH
)

v2=ChromaDB.load_document(
    embedding_model=embedding,
    dir=project_root+Config.VECTORSTORE2_PATH
)



class search_by_id:
    def __init__(self):
        pass

    def run(self,ID:str):
        """
        search_by_id:根据患者id在数据库查询其曾经的体检信息
        Args:
        ID (str): 唯一标识用户的六位数ID
        """
        result = v1.query_data("患者ID:{}".format(ID), query_num=1)
        result = merge_content(result)
        check = result[5:11]
        if check != ID:
            result = "没有找到该患者曾经的的体检信息"
        return result
    


class search_by_other:
    def __init__(self):
        pass

    def run(self,num:int, user_info:str):
        """
        search_by_other:根据患者个人信息在数据库查询相似病人体检信息
        Args:
        num (int): 需要查询的相似体检信息数量(不超过5)
        user_info (str): 用户输入的除ID外全部个人信息，格式为"性别,年龄(岁),身高(cm),体重(kg),既往病史,症状"
        """
        result = v1.query_data(user_info, query_num=int(num))
        result = merge_content(result)
        return result
    


class recommend_by_age:
    def __init__(self):
        pass

    def run(self,age:int):
        """
        recommend_by_age:根据患者的年龄阶段推荐不同的体检项目
        Args:
        age (int): 患者年龄
        """
        age = int(age)
        if(age <= 18):
            result = "建议关注生长发育、视力、营养、心理健康等方面的检查"
        elif(age > 18 and age <= 40):
            result = "建议关注体重、血压、血糖、血脂、甲状腺功能、颈椎腰椎的检查"
        elif(age > 40 and age <= 60):
            result = "建议关注心脑血管、肿瘤标志物、骨密度及其他慢性病的检查"
        elif(age > 60):
            result = "建议加强肿瘤筛查、心脑血管检查、胃肠镜检查，同时进行认知功能衰退评估"
        return result



class recommend_by_gender:
    def __init__(self):
        pass

    def run(self,gender:str):
        """
        recommend_by_gender:根据患者的性别推荐不同的体检项目
        Args:
        age (int): 患者性别(male/female)
        """
        if(gender=="male"):
            result = "建议男性关注前列腺、肝脏、心脑血管、肺部、生殖系统等方面的检查"
        elif(gender == "female"):
            result = "建议女性关注乳腺、宫颈、妇科等方面的检查"
        else:
            result = "性别输入有误，请输入'male'或'female'"
        return result