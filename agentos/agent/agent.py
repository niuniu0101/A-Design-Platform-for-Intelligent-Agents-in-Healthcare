import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)

import inspect

from agentos.memory import TemporaryMemory,Message,Role
from agentos.prompt import DEFAULT_PROMPT

from typing import List

from agentos.utils import call_model


def parse_tool_info(tools):
    info = ""
    for index, tool in enumerate(tools):
        # info = info+(index+1)+".\n"
        info = info+"\nfunction "+str(index+1)+".\n"
        # info = info+tool.run.__doc__
        info = info+inspect.cleandoc(tool.run.__doc__)
    return info
     
    

class Agent:
    def __init__(
        self,
        name:str=None,
        model:dict=None,
        tools:List=None,
        api_key: str | None = None,
    ):
        self.name = name
        self.model = model
        self.api_key = api_key

        self.tools={}
        for tool in tools:
            self.tools[tool.__class__.__name__]=tool
         
        
        self.memory = TemporaryMemory()

        tool_info = ""
        if tools is not None:
            tool_info=parse_tool_info(tools)
        
         
        self.memory.add_memory(Message(Role.SYSTEM,DEFAULT_PROMPT.format(tool_info)))
        #print(self.memory.memory[0]['content'])
    def call_tool(
        self,
        tool_name:str,
        tool_args:List
    ):
        return str(self.tools[tool_name].run(*tool_args))

    def reason(
        self,
    ):
        
        response = call_model(self.memory.memory,self.api_key) #需要改这里
        
        self.memory.add_memory(Message(Role.ASSISTANT,response))
        # print(response)

        #parse response
        thought = ""
        tool_name = ""
        tool_args = []
        for id, line in enumerate(response.splitlines(), start=1):
            if(id==1):
                thought = line.split(":")[1].lstrip()
            elif(id==2):
                tool_name = line.split(":")[1].lstrip()
            else:
                arg = line.split(":")[1].lstrip()
                tool_args.append(arg)
                
        print(response)        
        return thought,tool_name,tool_args
    
    def act(
        self,
        tool_name:str,
        tool_args:List
    ):
        print(f"call tool:{tool_name}\nargs:{tool_args}")
        # print()
        
        tool_call_res = self.call_tool(tool_name,tool_args)
        self.memory.add_memory(Message(Role.USER,"The "+tool_name+" function has been executed and the result is below:\n"+tool_call_res))
        
        print(f"tool_call_res:\n{tool_call_res}")

        return True    
         
    

    def run(
        self,
        task:str,
    ):
        self.memory.add_memory(Message(Role.USER,task))
          
        while(True):
            print("-----------------------------reason-----------------------------")
            thought,tool_name,tool_args=self.reason()
            if(tool_name=='finish'):
                break

            print("------------------------------act-------------------------------")
            self.act(tool_name,tool_args)

           

           
             






 