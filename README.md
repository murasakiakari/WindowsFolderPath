# WindowsFolderPath
This library is base on the idea original from https://gist.github.com/mkropat/7550097 and https://stackoverflow.com/a/35851955.  
This library is designed to run on Windows and used to find the path of 
**Desktop, Documents, Downloads, Music, Pictures and Videos folders only.**  
**This is also a wheel that reinvented under the consideration of learning and practicing.**
## Usages
### Example Command
<pre>
from WindowsFolderPath import WindowsFolderPath
print(WindowsFolderPath().Desktop())
# C:\Users\user\Desktop
print(WindowsFolderPath().Downloads())
# E:\ (In my case)</pre>
