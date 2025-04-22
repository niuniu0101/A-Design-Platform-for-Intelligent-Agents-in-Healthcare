import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

# print(project_root)

from agentos.agent.agent import Agent
from agentos.memory import TemporaryMemory,Message,Role
from test.test_tools import *

myagent = Agent(
    name="myagent",
    model={},
    tools=[calculator(),weather()]
) 



# print(myagent.memory.memory[0]['content'])
# print(myagent.tools)

# myagent.memory.add_memory(Message(Role.USER,"我在武汉洪山区，今天想出去打篮球，请问天气合适吗？"))
# thought,tool_name,tool_args =myagent.reason()
# print("================\n")
# print(thought,"\n-------\n",tool_name,"\n-------\n",tool_args)



# myagent.memory.add_memory(Message(Role.USER,"我在武汉洪山区，今天想出去打篮球，请问天气合适吗？我还想计算1+1。"))
# thought,tool_name,tool_args =myagent.reason()
# myagent.act(tool_name,tool_args)
# print("================\n")
# thought,tool_name,tool_args =myagent.reason()
# myagent.act(tool_name,tool_args)



myagent.run("我在武汉洪山区，请问今天天气怎么样？我还想计算1+1。")
print("\n=============================MRMORY=============================")
for i in myagent.memory.memory:
    print(i['role'])
    print(i['content'])
    print("------------")