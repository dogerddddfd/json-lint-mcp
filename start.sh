#!/bin/bash

# 激活虚拟环境（使用相对于脚本所在目录的明确路径）
source "$(dirname "$0")/venv/bin/activate"

# 启动 MCP 服务（确保使用与虚拟环境绑定的 Python）
cd "$(dirname "$0")"
"$(dirname "$0")/venv/bin/python" -m src.main
