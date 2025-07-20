# Retrieval Augmented Generation (RAG) System
# 检索增强生成 (RAG) システム
# 检索增强生成 (RAG) 系统

## 📖 Project Introduction / 项目简介 / プロジェクト紹介

This project implements a Retrieval Augmented Generation (RAG) system with multiple AI agents, inspired by the Machine Learning 2025 Spring course at National Taiwan University.

本项目实现了基于多AI代理的检索增强生成(RAG)系统，参考台湾大学2025年春季机器学习课程。

このプロジェクトは、台湾大学2025年春学期機械学習コースを参考に、複数のAIエージェントを使用した検索拡張生成(RAG)システムを実装しています。

**Reference Course**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)

## 🚀 Features / 功能特性 / 機能

### Core Features / 核心功能 / コア機能
- 🤖 **Multi-Agent System**: Question extraction, keyword extraction, QA, and answer verification agents
- 🔍 **Web Search Integration**: Real-time information retrieval from the internet
- 📚 **RAG Pipeline**: Complete retrieval-augmented generation workflow
- 🎯 **Dual Environment Support**: Local CPU and Colab GPU versions
- 🔄 **Asynchronous Processing**: Efficient handling of multiple requests

### 多代理系统 / マルチエージェントシステム
- 🤖 **问题提取代理**: 从复杂问题中提取核心内容
- 🔍 **关键词提取代理**: 识别最重要的搜索关键词
- 📝 **问答代理**: 基于知识库和检索信息生成答案
- ✅ **答案验证代理**: 确保答案的准确性和逻辑性

## 📁 Project Structure / 项目结构 / プロジェクト構造

```
retrieval_augmented_generation/
├── README.md                    # Main documentation / 主说明文档 / メインドキュメント
├── start_local.py               # Startup script / 启动脚本 / 起動スクリプト
├── localversion_cpucode/        # Local CPU version / 本地CPU版本 / ローカルCPU版
│   ├── run_rag.py              # Main runner / 主运行脚本 / メイン実行スクリプト
│   ├── requirements_local.txt   # Local dependencies / 本地依赖 / ローカル依存関係
│   └── README_local.md         # Local version guide / 本地版本说明 / ローカル版ガイド
├── colab_GPUcode/              # Colab GPU version / Colab GPU版本 / Colab GPU版
│   ├── retrieval_augmented_generation_w_agents.py
│   ├── requirements.txt        # Colab dependencies / Colab依赖 / Colab依存関係
│   └── README.md              # Colab version guide / Colab版本说明 / Colab版ガイド
└── shared_data/                # Shared data files / 共享数据文件 / 共有データファイル
    ├── Meta-Llama-3.1-8B-Instruct-Q8_0.gguf
    ├── public.txt             # Public test questions / 公开测试问题 / 公開テスト問題
    └── private.txt            # Private test questions / 私有测试问题 / プライベートテスト問題
```

## 🎯 Quick Start / 快速开始 / クイックスタート

### Local CPU Version / 本地CPU版本 / ローカルCPU版
```bash
cd retrieval_augmented_generation
python3 start_local.py
```

### Colab GPU Version / Colab GPU版本 / Colab GPU版
1. Upload `colab_GPUcode/` folder to Google Drive
2. Run `retrieval_augmented_generation_w_agents.py` in Colab

## 📊 Version Comparison / 版本对比 / バージョン比較

| Feature / 特性 / 機能 | Local CPU / 本地CPU / ローカルCPU | Colab GPU / Colab GPU / Colab GPU |
|----------------------|-----------------------------------|-----------------------------------|
| Hardware Requirements / 硬件要求 / ハードウェア要件 | CPU + 8GB RAM | GPU + Colab Environment |
| Speed / 速度 / 速度 | Slow (1-3s/question) | Fast (0.5-1s/question) |
| Network Dependency / 网络依赖 / ネットワーク依存 | Model download required | Internet connection required |
| Cost / 成本 / コスト | Free | Colab quota required |
| Privacy / 隐私 / プライバシー | Fully local | Data in cloud |

## 🔧 System Requirements / 系统要求 / システム要件

### Local CPU Version / 本地CPU版本 / ローカルCPU版
- Python 3.8+
- 8GB+ RAM
- 10GB+ storage space
- Stable internet connection (for initial download)

### Colab GPU Version / Colab GPU版本 / Colab GPU版
- Google Colab account
- GPU runtime
- Internet connection

## 📝 Features / 功能特性 / 機能特性

- ✅ 4-Agent collaboration system
- ✅ Multi-strategy web search
- ✅ Intelligent content filtering
- ✅ Answer quality verification
- ✅ Asynchronous processing
- ✅ Error recovery mechanism

## 🎯 Use Cases / 使用场景 / ユースケース

- **Local CPU Version**: Development testing, offline use, privacy-sensitive scenarios
- **Colab GPU Version**: Rapid prototyping, batch processing, cloud deployment


## 📚 Academic Reference / 学术参考 / 学術参考

This project is based on the Machine Learning 2025 Spring course at National Taiwan University, specifically Homework 1: AI Agent1 -- RAG.

本项目基于台湾大学2025年春季机器学习课程，特别是作业1：AI Agent1 -- RAG。

このプロジェクトは、台湾大学2025年春学期機械学習コース、特に宿題1：AI Agent1 -- RAGに基づいています。

**Course Link**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)
**Instructor**: Prof. Hung-yi Lee (李宏毅教授)
**Course**: Machine Learning 2025 Spring
**Homework**: HW1 - AI Agent1 -- RAG
