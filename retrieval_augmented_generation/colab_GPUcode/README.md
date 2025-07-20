# ML2025 Homework 1 - Retrieval Augmented Generation with Agents
# ML2025 作业1 - 基于代理的检索增强生成
# ML2025 宿題1 - エージェントを使用した検索拡張生成

## 📖 Project Introduction / 项目简介 / プロジェクト紹介

This is a question-answering system based on Retrieval Augmented Generation (RAG) that implements the following features:

这是一个基于检索增强生成(RAG)的问答系统，实现了以下功能：

これは検索拡張生成(RAG)に基づく質問応答システムで、以下の機能を実装しています：

- 🤖 **LLM Model Inference**: Uses LLaMA 3.1 8B model for text generation
- 🔍 **Web Search**: Integrates Google Search API for real-time information
- 🤝 **Multi-Agent System**: Different professional agents collaborate to process questions
- 🔄 **RAG Pipeline**: Complete question-answering workflow combining retrieval and generation

**Reference Course**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)

## 🚀 Local Running Instructions / 本地运行说明 / ローカル実行説明

### System Requirements / 系统要求 / システム要件
- **Python**: 3.8+
- **Memory**: At least 8GB (16GB+ recommended)
- **Storage**: At least 10GB available space (model file ~8GB)
- **GPU**: Optional but strongly recommended for better performance
- **Network**: Stable network connection (for downloading models and searching)

### 📦 Installation Steps / 安装步骤 / インストール手順

#### 1. Environment Preparation / 环境准备 / 環境準備
```bash
# Clone or download project files
# Ensure you're in the project directory

# Install dependency packages
pip install -r requirements.txt
```

#### 2. Run Test Version (Recommended first) / 运行测试版本（推荐先运行）/ テスト版実行（最初に推奨）
```bash
python test_local.py
```

**Test Version Features / 测试版本功能 / テスト版機能**:
- ✅ Automatically check and install necessary Python packages
- 📥 Automatically download LLaMA 3.1 8B model file (~8GB)
- 🔍 Check GPU environment
- 🤖 Test basic LLM inference functionality
- 📊 Display performance information

#### 3. Run Complete Version / 运行完整版本 / 完全版実行
```bash
python retrieval_augmented_generation_w_agents.py
```

**Complete Version Features / 完整版本功能 / 完全版機能**:
- 🔍 Web search enhancement
- 🤝 Multi-agent collaboration
- 📚 Batch processing of test questions
- 💾 Automatic result saving
- 🔄 Checkpoint resume support

### ⚠️ Important Notes / 注意事项 / 重要な注意事項

#### 1. Model File Download / 模型文件下载 / モデルファイルダウンロード
- 📥 **File Size**: ~8GB (LLaMA 3.1 8B quantized model)
- ⏱️ **Download Time**: Depends on network speed, may take 10-30 minutes
- 💾 **Storage Space**: Ensure at least 10GB available space
- 🔄 **Resume Download**: If download is interrupted, re-running will automatically skip already downloaded parts

#### 2. GPU Usage / GPU使用 / GPU使用
- 🎯 **Auto-Detection**: Code automatically detects if GPU is available
- ⚡ **Performance Boost**: GPU can significantly improve inference speed (10-100x)
- 🔧 **CPU Fallback**: Automatically uses CPU when no GPU is available (slower but usable)
- 💡 **Recommendation**: If you have GPU, ensure CUDA and PyTorch GPU version are installed

#### 3. Student ID Setting / 学号设置 / 学籍番号設定
Before running the complete version, please modify the student ID in the code:
```python
# Find this line in retrieval_augmented_generation_w_agents.py
STUDENT_ID = ""  # Change to your student ID, e.g., "B123456789"
```

#### 4. Network Connection / 网络连接 / ネットワーク接続
- 🌐 **Download Requirements**: Network connection needed for downloading models and data files
- 🔍 **Search Function**: Web search function requires stable network connection
- ⚠️ **Rate Limiting**: Google search has rate limits, frequent searches may be temporarily banned

#### 5. Memory Usage / 内存使用 / メモリ使用量
- 💾 **Model Loading**: Model loading requires large memory (8-16GB)
- 🔄 **Inference Process**: Inference process will occupy additional memory
- 💡 **Recommendation**: Close other memory-consuming programs

## 📁 File Description / 文件说明 / ファイル説明

| Filename / 文件名 / ファイル名 | Description / 说明 / 説明 | Purpose / 用途 / 用途 |
|-------------------------------|---------------------------|----------------------|
| `retrieval_augmented_generation_w_agents.py` | Main program file | Complete RAG system implementation |
| `requirements.txt` | Dependency package list | Automatically install required Python packages |
| `README.md` | Detailed documentation | Usage guide and troubleshooting |

## 🔧 Code Structure Explanation / 代码结构说明 / コード構造説明

#### Main Components / 主要组件 / 主要コンポーネント
1. **Environment Management**: Automatic dependency installation, model file download
2. **LLM Inference**: LLaMA model loading and text generation
3. **Search Tools**: Google Search API integration
4. **Agent System**: Multi-professional agent collaboration
5. **RAG Pipeline**: Retrieval-augmented generation workflow
6. **Batch Processing**: Automatic processing of test question sets

## 🔧 Troubleshooting / 故障排除 / トラブルシューティング

#### 1. Insufficient Memory / 内存不足 / メモリ不足
**Symptoms**: Program crashes or reports memory errors
**Solutions**:
- 💾 Reduce `n_ctx` parameter value (search for `n_ctx=16384` in code)
- 🔄 Close other memory-consuming programs
- 📉 Use smaller model (requires modifying model file)

#### 2. Download Failure / 下载失败 / ダウンロード失敗
**Symptoms**: Model file download fails
**Solutions**:
- 🌐 Check network connection
- 🔄 Re-run program (supports resume download)
- 📥 Manually download model file to current directory
- 🔗 Use VPN or proxy

#### 3. Package Installation Failure / 包安装失败 / パッケージインストール失敗
**Symptoms**: pip package installation errors
**Solutions**:
- 🔄 Update pip: `pip install --upgrade pip`
- 🐍 Use conda environment (recommended)
- 🔧 Check Python version compatibility
- 📦 Manually install problematic packages

#### 4. GPU-Related Issues / GPU相关问题 / GPU関連の問題
**Symptoms**: GPU detection fails or CUDA errors
**Solutions**:
- 🔧 Install CUDA and cuDNN
- 📦 Install PyTorch GPU version
- 🔄 Restart system
- 💻 Check GPU drivers

#### 5. Search Function Issues / 搜索功能问题 / 検索機能の問題
**Symptoms**: Search returns errors or 429 status code
**Solutions**:
- ⏱️ Wait a while and retry (rate limiting)
- 🌐 Check network connection
- 🔄 Reduce search frequency
- 🔧 Use proxy or VPN

## ⚡ Performance Optimization Suggestions / 性能优化建议 / パフォーマンス最適化の提案

#### Hardware Optimization / 硬件优化 / ハードウェア最適化
1. **GPU Acceleration**: Use CUDA-supported GPU
2. **Memory Upgrade**: Increase to 16GB or more
3. **SSD Storage**: Use SSD to improve file read/write speed
4. **CPU Optimization**: Use multi-core CPU

#### Software Optimization / 软件优化 / ソフトウェア最適化
1. **Parameter Adjustment**: Adjust model parameters based on hardware
2. **Batch Processing**: Process questions in batches instead of one by one
3. **Caching Mechanism**: Cache search results to avoid duplicate requests
4. **Parallel Processing**: Use multi-process or multi-thread

## 📞 Getting Help / 获取帮助 / ヘルプの取得

If you encounter problems, please:
1. 📖 Carefully read error messages
2. 🔍 Check the troubleshooting section
3. 📝 Record detailed error logs
4. 💬 Seek help in course forums or GitHub Issues

---

## 📚 Academic Reference / 学术参考 / 学術参考

This implementation is based on the Machine Learning 2025 Spring course at National Taiwan University, specifically Homework 1: AI Agent1 -- RAG.

此实现基于台湾大学2025年春季机器学习课程，特别是作业1：AI Agent1 -- RAG。

この実装は、台湾大学2025年春学期機械学習コース、特に宿題1：AI Agent1 -- RAGに基づいています。

**Course Link**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)
**Instructor**: Prof. Hung-yi Lee (李宏毅教授)
**Course**: Machine Learning 2025 Spring
**Homework**: HW1 - AI Agent1 -- RAG 