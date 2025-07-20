#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG System Startup Script / RAG系统启动脚本 / RAGシステム起動スクリプト

This script provides an easy way to run the RAG system with different options.
このスクリプトは、異なるオプションでRAGシステムを簡単に実行する方法を提供します。
此脚本提供了运行RAG系统的便捷方式，支持不同选项。

Features / 功能 / 機能:
- Test mode: Quick environment check and basic functionality test
- Full run: Complete RAG pipeline execution
- Project structure display: Show organized file structure

Reference Course: Machine Learning 2025 Spring - NTU
参考课程: 台湾大学2025年春季机器学习课程
参考コース: 台湾大学2025年春学期機械学習コース
Course Link: https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """主启动函数"""
    print("🚀 RAG系统启动器")
    print("=" * 50)
    
    # 检查当前目录
    current_dir = Path.cwd()
    if current_dir.name != "retrieval_augmented_generation":
        print("❌ 请在 retrieval_augmented_generation 目录下运行此脚本")
        print(f"当前目录: {current_dir}")
        return
    
    # 检查虚拟环境
    venv_path = Path("../rag_env")
    if not venv_path.exists():
        print("❌ 未找到虚拟环境，请先创建虚拟环境")
        print("运行: python3 -m venv rag_env")
        return
    
    # 检查共享数据
    shared_data = Path("shared_data")
    if not shared_data.exists():
        print("❌ 未找到共享数据目录")
        return
    
    model_file = shared_data / "Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"
    if not model_file.exists():
        print("❌ 未找到模型文件")
        print(f"请确保模型文件存在于: {model_file}")
        return
    
    print("✅ 环境检查通过")
    print("\n选择运行模式:")
    print("1. 测试模式 (单个问题)")
    print("2. 完整运行 (所有问题)")
    print("3. 查看项目结构")
    print("4. 退出")
    
    choice = input("\n请输入选择 (1-4): ").strip()
    
    if choice == "1":
        print("\n🧪 启动测试模式...")
        os.chdir("localversion_cpucode")
        subprocess.run([sys.executable, "run_rag.py", "test"])
        
    elif choice == "2":
        print("\n🎯 启动完整运行...")
        os.chdir("localversion_cpucode")
        subprocess.run([sys.executable, "run_rag.py"])
        
    elif choice == "3":
        print("\n📁 项目结构:")
        print("retrieval_augmented_generation/")
        print("├── README.md                    # 主说明文档")
        print("├── start_local.py               # 启动脚本")
        print("├── localversion_cpucode/        # 本地CPU版本代码")
        print("│   ├── run_rag.py              # 主运行脚本")
        print("│   ├── simple_test.py          # 测试脚本")
        print("│   ├── requirements_local.txt   # 本地依赖")
        print("│   └── README_local.md         # 本地版本说明")
        print("├── colab_GPUcode/              # Colab GPU版本代码")
        print("│   ├── retrieval_augmented_generation_w_agents.py")
        print("│   ├── requirements.txt        # Colab依赖")
        print("│   └── README.md              # Colab版本说明")
        print("└── shared_data/                # 共享数据文件")
        print("    ├── Meta-Llama-3.1-8B-Instruct-Q8_0.gguf")
        print("    ├── public.txt             # 公开测试问题")
        print("    └── private.txt            # 私有测试问题")
        
    elif choice == "4":
        print("👋 再见！")
        
    else:
        print("❌ 无效选择")

if __name__ == "__main__":
    main() 