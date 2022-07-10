# tinyMediaManager（tmm）辅助脚本

## 脚本介绍
此脚本主要用于定位额外内容文件夹，并在其中创建`.tmmignore`文件。
- 收藏动漫BD时，除去正片，各家字幕组都会打包PV、SP等额外内容。
- tmm刮削时会把这些内容和正片混在一起，增加额外的工作量。
- 在文件夹中放入`.tmmignore`文件，tmm在扫描时会忽略此文件夹。


## 工作逻辑
- 脚本会遍历根目录下所有目录，首先根据关键词找到额外内容文件夹。
  - 关键词包含了各家字幕组惯用命名，如'SPs','extra','bonus','映像特典'等，可自行修改。
- 为了减少改动，脚本仅在含有视频文件的额外内容文件夹中创建`.tmmignore`文件。

- 所有被标记的文件夹路径保存在当前文件夹的`tmmignoreList.txt`文件中，方便查看与后续更新。
- 若脚本运行时，当前文件夹已存在`tmmignoreList.txt`，
  - 脚本会载入该文件，在扫描时忽略其中的文件夹以提升效率，并在执行后更新该文件。
- 若脚本新标记了`tmmignoreList.txt`之外的文件夹，
  - 脚本会添加这些文件夹路径，并额外创建`tmmignoreList_new.txt`方便查看。

## 安全声明
- 脚本仅会创建与修改脚本相关的三个文件，对其他文件、目录仅进行查看操作。
  - `.tmmignore` 空文件，不含任何内容
  - `tmmignoreList.txt` 日志文件
  - `tmmignoreList_new.txt` 日志文件

## 运行方法
1. 根目录运行
下载脚本并至视频根目录（如：E:\animes），在脚本所在位置打开CMD，输入如下指令
```
$ python tmmignore_add2extras.py
```

2. 其他目录运行
下载脚本到任意文件夹，在脚本所在位置打开CMD，输入如下指令。\[根目录路径]指视频存放目录（如：E:\animes）
```
$ python tmmignore_add2extras.py [根目录路径]
  # e.g.
$ python tmm ignore_add2extras.py E:\animes
```

## 进阶定制
脚本仅根据个人经验定义了常见关键词（匹配时不区分大小写）：  
- 额外内容文件夹命名关键词（list_tmmignFolderKeys）
- 视频后缀类型关键词（list_videoSuffixes）

如有需要请修改代码开头如下部分。  
```
list_tmmignFolderKeys = ['sp','extra','bonus','mv','bd','pv','menu','preview','other','creditless','映像特典','次回予告']
list_videoSuffixes = ['mkv','avi','mp4','rmvb']
```
