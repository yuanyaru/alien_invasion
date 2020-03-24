# alien_invasion
项目 “外星人入侵” ，是使用Pygame包开发的一款2D游戏，它在玩家每消灭一群向下移动的外星人后，都将玩家提高一个等级；等级越高，游戏的节奏越快，难度越大。

## 打包说明
1.安装 pyinstaller 工具
```bash
pip install pyinstaller     
```
2.打包
pyinstaller -F alien_invasion.py<要打包的py文件>

避免出现找不到图片或打开游戏闪退问题，需要注意：
1. 图片路径
2. 字体设置