import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.json_lint import validate_json, validate_file

def test_valid_json_content():
    """测试有效的 JSON 内容"""
    print("\n=== 测试有效的 JSON 内容 ===")
    json_content = '{"name": "test", "value": 123}'
    success, data, error_msg = validate_json(json_content)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == True
    assert data is not None
    assert error_msg is None
    print("✓ 测试通过")

def test_invalid_json_content():
    """测试无效的 JSON 内容"""
    print("\n=== 测试无效的 JSON 内容 ===")
    json_content = '{"name": "test", "value": }'
    success, data, error_msg = validate_json(json_content)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == False
    assert data is None
    assert error_msg is not None
    print("✓ 测试通过")

def test_valid_json_file():
    """测试有效的 JSON 文件"""
    print("\n=== 测试有效的 JSON 文件 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_valid.json')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == True
    assert data is not None
    assert error_msg is None
    print("✓ 测试通过")

def test_invalid_json_file():
    """测试无效的 JSON 文件"""
    print("\n=== 测试无效的 JSON 文件 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_invalid.json')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == False
    assert data is None
    assert error_msg is not None
    print("✓ 测试通过")

def test_invalid_json_file_2():
    """测试无效的 JSON 文件"""
    print("\n=== 测试无效的 JSON 文件 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_invalid_2.json')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == False
    assert data is None
    assert error_msg is not None
    print("✓ 测试通过")

def test_valid_ipynb_file():
    """测试有效的 ipynb 文件"""
    print("\n=== 测试有效的 ipynb 文件 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_valid.ipynb')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == True
    assert data is not None
    assert error_msg is None
    print("✓ 测试通过")

def test_invalid_ipynb_file():
    """测试无效的 ipynb 文件"""
    print("\n=== 测试无效的 ipynb 文件 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_invalid.ipynb')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == False
    assert data is None
    assert error_msg is not None
    print("✓ 测试通过")

def test_ipynb_escape_error():
    """测试 ipynb 文件中 JSON 反义符缺失的情况"""
    print("\n=== 测试 ipynb 文件中 JSON 反义符缺失 ===")
    file_path = os.path.join(os.path.dirname(__file__), 'test_ipynb_escape_error.ipynb')
    success, data, error_msg = validate_file(file_path)
    print(f"成功: {success}")
    print(f"数据: {data}")
    print(f"错误: {error_msg}")
    assert success == False
    assert data is None
    assert error_msg is not None
    print("✓ 测试通过")

if __name__ == "__main__":
    print("开始测试 JSON 验证逻辑...")
    
    try:
        test_valid_json_content()
        test_invalid_json_content()
        test_valid_json_file()
        test_invalid_json_file()
        test_invalid_json_file_2()
        test_valid_ipynb_file()
        test_invalid_ipynb_file()
        test_ipynb_escape_error()
        
        print("\n🎉 所有测试通过！")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
