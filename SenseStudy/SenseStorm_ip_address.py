import os
result=os.popen('ifconfig').read()
print(result)
