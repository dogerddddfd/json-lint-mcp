from fastmcp import FastMCP
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv
from .json_lint import validate_json, validate_file

# 加载 .env 文件
load_dotenv()

# 创建 FastMCP 实例
app = FastMCP(name="JSON Lint MCP")


# 注册工具
@app.tool
def json_lint(
    file_path: Optional[str] = None,
    content: Optional[str] = None
) -> Dict[str, Any]:
    """
    检查 JSON 或 ipynb 文件的格式正确性
    
    Args:
        file_path: 文件路径
        content: 待验证的 JSON 字符串
            注意：file_path 与 content 不能同时提供，否则函数会返回错误
    
    Returns:
        Dict[str, Any]: 包含验证结果的字典
            - success: bool，验证是否成功
            - error: str，错误信息（如果失败）
            - file_path: str，验证的文件路径（如果提供）
    """
    # 验证参数
    if not file_path and not content:
        return {
            "success": False,
            # "data": None,
            "error": "必须提供 file_path 或 content 参数",
            "file_path": file_path
        }
    # 如果同时提供 file_path 和 content，返回错误
    if file_path and content:
        return {
            "success": False,
            # "data": None,
            "error": "不能同时提供 file_path 和 content 参数",
            "file_path": file_path
        }
    # 处理文件路径
    if file_path:
        success, data, error_msg = validate_file(file_path)
        return {
            "success": success,
            # "data": data,
            "error": error_msg,
            "file_path": file_path
        }
    
    # 处理内容
    if content:
        success, data, error_msg = validate_json(content)
        return {
            "success": success,
            # "data": data,
            "error": error_msg,
            "file_path": None
        }
    
    # 理论上不会到达这里
    return {
        "success": False,
        # "data": None,
        "error": "参数错误",
        "file_path": file_path
    }


# 启动服务
if __name__ == "__main__":
    # 从环境变量读取配置
    app.run(transport="stdio")
