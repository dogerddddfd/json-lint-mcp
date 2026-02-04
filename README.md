# JSON Lint MCP

一个用于检查~~便宜~~AI生成的长篇 JSON（包括 ipynb）文件格式，以及 JSON 格式字符串正确性的MCP服务。

~~求求你了写对反义符吧~~

## 功能特性

- 使用fastmcp框架
- 检查 JSON 字符串的格式正确
- 检查 JSON / ipynb 文件的格式正确性
- 提供详细的错误信息，包括错误位置和上下文
- 支持 stdio 和 http 两种传输方式

## 安装

1. 克隆项目

2. 创建并激活虚拟环境
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

4. 配置环境变量`.env`

## 配置

项目使用 `.env` 文件进行配置，主要配置项如下：

- `MCP_TRANSPORT`：传输方式，可选值为 `stdio`（默认）或 `http`
- `MCP_HOST`：HTTP 传输时的主机地址，默认为 `0.0.0.0`
- `MCP_PORT`：HTTP 传输时的端口，默认为 `8000`

## 使用

### 启动 MCP 服务

使用 `start.sh` 脚本启动 MCP 服务：

```bash
chmod +x start.sh
```

```bash
./start.sh
```


## 许可证

MIT
