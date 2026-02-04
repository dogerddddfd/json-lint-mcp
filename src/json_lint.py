import json
import os
from typing import Dict, Any, Optional, Tuple, List


def validate_json(content: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    验证 JSON 字符串的格式正确性
    
    Args:
        content: JSON 字符串内容
    
    Returns:
        Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
            - 第一个元素：验证是否成功
            - 第二个元素：解析后的 JSON 对象（如果成功）
            - 第三个元素：错误信息（如果失败）
    """
    try:
        data = json.loads(content)
        return True, data, None
    except json.JSONDecodeError as e:
        # 构建详细的错误信息
        error_msg = f"JSON 格式错误: {e.msg}"
        error_msg += f"\n位置: 第 {e.lineno} 行, 第 {e.colno} 列"
        
        # 尝试获取错误行的上下文
        lines = content.splitlines()
        if 0 < e.lineno <= len(lines):
            error_line = lines[e.lineno - 1]
            error_msg += f"\n错误行: {error_line.strip()}"
            # 添加指向错误位置的标记
            if e.colno > 0:
                error_msg += f"\n{' ' * (e.colno - 1)}^"
        
        return False, None, error_msg



def validate_json_file(file_path: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    验证 JSON 文件的格式正确性
    
    Args:
        file_path: JSON 文件路径
    
    Returns:
        Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
            - 第一个元素：验证是否成功
            - 第二个元素：解析后的 JSON 对象（如果成功）
            - 第三个元素：错误信息（如果失败）
    """
    if not os.path.exists(file_path):
        return False, None, f"文件不存在: {file_path}"
    
    if not os.path.isfile(file_path):
        return False, None, f"路径不是文件: {file_path}"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return validate_json(content)
    except Exception as e:
        return False, None, f"文件读取错误: {str(e)}"



def validate_ipynb_file(file_path: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    验证 ipynb 文件的格式正确性
    
    Args:
        file_path: ipynb 文件路径
    
    Returns:
        Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
            - 第一个元素：验证是否成功
            - 第二个元素：解析后的 JSON 对象（如果成功）
            - 第三个元素：错误信息（如果失败）
    """
    # 首先验证文件扩展名
    if not file_path.endswith('.ipynb'):
        return False, None, f"文件不是 ipynb 文件: {file_path}"
    
    # 然后验证 JSON 格式
    success, data, error_msg = validate_json_file(file_path)
    if not success:
        return success, data, error_msg
    
    # 验证 ipynb 文件的基本结构
    if not isinstance(data, dict):
        return False, None, "ipynb 文件必须是一个 JSON 对象"
    
    # 检查必要的字段
    if 'cells' not in data:
        return False, None, "ipynb 文件缺少 'cells' 字段"
    
    if 'metadata' not in data:
        return False, None, "ipynb 文件缺少 'metadata' 字段"
    
    if 'nbformat' not in data:
        return False, None, "ipynb 文件缺少 'nbformat' 字段"
    
    if 'nbformat_minor' not in data:
        return False, None, "ipynb 文件缺少 'nbformat_minor' 字段"
    
    return True, data, None


def validate_file(file_path: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    根据文件扩展名验证文件格式
    
    Args:
        file_path: 文件路径
    
    Returns:
        Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
            - 第一个元素：验证是否成功
            - 第二个元素：解析后的 JSON 对象（如果成功）
            - 第三个元素：错误信息（如果失败）
    """
    if file_path.endswith('.ipynb'):
        return validate_ipynb_file(file_path)
    else:
        return validate_json_file(file_path)
