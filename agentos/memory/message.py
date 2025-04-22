from enum import Enum

 
class Role(Enum):
    SYSTEM = "system" 
    USER = "user" 
    ASSISTANT = "assistant" 
    TOOL = "tool"
 

class Message:
    def __init__(
        self,
        role:Enum,
        content:str
    ):
        self.role = role.value
        self.content=content
        
    
     
  