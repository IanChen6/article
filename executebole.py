from scrapy.cmdline import execute

import sys
import os
# sys.path.append(" sys.path.append(G:\新建文件夹 (2)\article)")
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))#file指当前Py文件，获取当前路径（绝对路径）
execute(['scrapy','crawl','bole'])