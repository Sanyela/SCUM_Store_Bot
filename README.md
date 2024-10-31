# SCUM Store Bot

一个基于Python的SCUM游戏服务器管理机器人，提供自动化的游戏管理功能。

## 主要功能

- 🎁 自动发送新手礼包
- 🚀 玩家传送系统（交易区/玩家互传）
- 💰 游戏币余额管理
- 👋 玩家进出服务器自动欢迎

## 技术栈

- Python 3.x
- Flask Web框架
- PyAutoGUI
- Win32API
- FTP协议
- 多线程处理

## 快速开始

### 环境要求

- Windows操作系统
- Python 3.x
- SCUM服务器

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/SCUM_Store_Bot.git
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置FTP连接：
修改配置文件中的FTP连接信息：
```python
FTP_HOST = "your_ftp_host"
FTP_PORT = "your_ftp_port"
FTP_USER = "your_username"
FTP_PASS = "your_password"
```

4. 运行程序：
```bash
python app.py
```

## API接口

### 传送服务
```
GET /tp_service/
参数：
- SteamID: 玩家Steam ID
- safe_area: 目标区域代码(A0/Z3/B4/C2)
```

### 玩家互传
```
GET /new_tp/
参数：
- SteamIDA: 发起者Steam ID
- SteamIDB: 目标玩家Steam ID
```

### 发放新手礼包
```
GET /new_people/
参数：
- SteamID: 玩家Steam ID
```

### 增加余额
```
GET /add_blance/
参数：
- SteamID: 玩家Steam ID
- num: 增加金额
```

## 项目结构

```
SCUM_Store_Bot/
├── app.py              # 主程序
├── requirements.txt    # 依赖列表
└── README.md          # 项目文档
```

## 注意事项

1. 运行时需确保SCUM服务器窗口可访问
2. 建议配置端口映射以供外网访问
3. 代码包含键盘锁定功能，请谨慎使用
4. 建议在专用服务器上运行

## 开发建议

- 本项目使用多线程处理并发
- 包含Windows窗口操作API
- 代码结构待优化
- 欢迎提交Pull Request改进代码

## 贡献指南

1. Fork 项目
2. 创建新分支
3. 提交更改
4. 发起Pull Request

## 许可证

MIT License

## 联系方式

如有问题，请提交Issue或联系开发者。

## 更新日志

### v1.0.0
- 基础功能实现
- 支持自动发送礼包
- 支持玩家传送
- 支持余额管理
- 支持进服欢迎

---
