import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

# print(project_root)

from agentos.agent.agent import Agent
from agentos.memory import TemporaryMemory,Message,Role
from src.tools import *
from src.hcr_prompt import HCR_PROMPT,OUTPUT_PROMPT
from agentos.utils import call_model


myagent = Agent(
    name="myagent",
    model={},
    tools=[]
) 

user_info ="id:123456\ngender:男\nage:25\nheight:180cm\nweight:70kg\nmedical_history:高血压\nsymptom:头晕"

myagent.run(HCR_PROMPT.format(user_info))

myagent.memory.add_memory(Message(Role.SYSTEM,OUTPUT_PROMPT))

print("\n==============================HCR===============================")
response=call_model(myagent.memory.memory)
print(response)
myagent.memory.add_memory(Message(Role.ASSISTANT,response))

print("\n=============================MRMORY=============================")
for i in myagent.memory.memory:
    print(f"【{i['role']}】")
    print(i['content'])
    print("------------")

