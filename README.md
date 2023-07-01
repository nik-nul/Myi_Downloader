# Myi_Downloader
基于python的轻量级少年派自主学习内容批量下载器
## 原理
使用[ibuprofen](https://github.com/Richard-Zheng/ibuprofen)获取的资源`json`信息进行解析，按照其内容下载文件
## 需求的库
* pandas：解析json数据
* json：解析json数据
* wget：下载文件
* os：进行文件操作
* re：使用正则表达式解析json数据
## 用法
1. 使用[ibuprofen](https://github.com/Richard-Zheng/ibuprofen)获取的`txt`格式的文件信息，复制到与`main.py`统一路径下  
   **注意：请提前将`\u200b`、`\u3000`、`\u00a0`等替换为空白或其他合法字符，否则作为非法字符将打断下载进程**  
           **若备课或文件名中有`/`、`\`、`*`、`<`、`>`、`"`、`|`、半角`:`、半角`?`等其他`Windows`系统的非法字符请自行删除或更换，否则也会打断下载进程**
3. 在此路径打开终端，并执行
   ```
   pip3 install -r requirements.txt
   python main.py
   ```
   **注意：`pip`指令下载的`wget`库无法正常使用，必须使用`pip3`指令下载**  
   **若出现`目标计算机积极拒绝`，请稍等片刻再重启程序，或检查学校服务器的连接情况**
5. 数据将自动保存在本路径下的`data`文件夹内，按照科目排列，科目下文件夹名为`备课发布时间`+`备课名`，内部为该备课全部文件
## 特性
* 按照与少年派相同的逻辑储存自主学习内容，便于检索
* 支持自动跳过已下载文件，初次建立数据库后可快速更新维护
* 实时显示下载进度
## 样例
在`demo`文件夹内有一个`txt`文档，该文档可作为调试本项目的样例数据  
经过测试，该样例可以在本人电脑上正常运行
## 一些废话
这是本人第一次制作类似项目，其实这就是一个json解释器，没有什么技术含量  
主要是我所在年级是最后一届使用睿易服务的  
其服务器不久即将关停  
为留存一些高中的回忆，仓促完成了此项目  
之前我并未学过`python`  
用这个小项目快速从零入门了`python`，还是比较有趣  
本项目可能仍存在若干问题  
希望您能积极提交`issue`，或者直接`pull request`  
这都将是对我莫大的鼓励(当然还有`star`(((
