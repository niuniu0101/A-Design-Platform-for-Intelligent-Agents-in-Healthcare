import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)


from agentos.memory.message import Message


class TemporaryMemory:
   
    def __init__(
        self
    ):    
        self.memory=[]

    def add_memory(
        self,
        msg:Message
    ): 
        self.memory.append({"role":msg.role,"content":msg.content})

    def clear(
        self
    ):
        self.memory=[]
    
    
            
        
        
         
    
        