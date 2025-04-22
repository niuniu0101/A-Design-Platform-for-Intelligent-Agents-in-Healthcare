import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)


#from flashrank import Ranker, RerankRequest
#from BCEmbedding import RerankerModel #https://huggingface.co/maidalun1020/bce-reranker-base_v1
from typing import List
from agentos.rag.data import BaseData,PdfData,TextData,JsonData,CsvData,merge_content
from sentence_transformers.cross_encoder import CrossEncoder

 

class Rerank:
    def __init__(
        self,
        model_name:str,
        cache_dir:str=None,
        **kwargs
    ):
        # cross-encoder/ms-marco-MiniLM-L6-v2
        # cache_folder="/mnt/7T/xz"
        self.ranker = CrossEncoder(model_name=model_name,cache_dir=cache_dir,**kwargs)
    
    def rerank(
        self,
        query:str,
        passages:List[str],
    ):
        sentence_pairs = [[query, passage] for passage in passages]
        rerank_results = self.ranker.rank(query, passages,return_documents=True)
        
        return rerank_results
    
 


