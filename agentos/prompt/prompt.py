DEFAULT_PROMPT = """\
Respond with specific tags as outlined below(The number of arguments is up to specific function):
thought:<what you thought>
function:<the function name you want to call>
argument1:<argument value>
argument2:<argument value>
...


The following tool functions are available in the format of
function index.
function name:function description
Args:
argument1(argument type):argument description
argument2(argument type):argument description
...


The function you can use：
function 0.
finish:If you think you finish the task,please call finish function.The function has not argument!{}


Please answer exactly according to the format mentioned at the beginning.Everytime you can just call one function.\
"""
 
 