# Local CPU Version RAG System Guide
# 本地CPU版本RAG系统使用指南
# ローカルCPU版RAGシステム使用ガイド

## 📖 Introduction / 简介 / 紹介

This is the local CPU version of the Retrieval Augmented Generation (RAG) system, designed to run on personal computers without requiring GPU acceleration.

这是检索增强生成(RAG)系统的本地CPU版本，专为在个人计算机上运行而设计，无需GPU加速。

これは検索拡張生成(RAG)システムのローカルCPU版で、GPUアクセラレーションを必要とせずにパーソナルコンピュータで実行するように設計されています。

**Reference Course**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)

## 🚀 Quick Start / 快速开始 / クイックスタート

### 1. System Requirements / 系统要求 / システム要件
- **Operating System**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **Memory**: At least 8GB RAM (16GB+ recommended)
- **Storage**: At least 10GB available space
- **Network**: Stable internet connection (for downloading models and searching)

### 2. Installation Steps / 安装步骤 / インストール手順

#### Method 1: Automatic Installation (Recommended) / 方法一：自动安装（推荐）/ 方法1：自動インストール（推奨）
```bash
# Run the main program directly, it will automatically install dependencies and download files
python run_rag.py
```

#### Method 2: Manual Installation / 方法二：手动安装 / 方法2：手動インストール
```bash
# 1. Install dependency packages
pip install -r requirements_local.txt

# 2. Run the main program
python run_rag.py
```

### 3. Running Tests / 运行测试 / テスト実行
```bash
# Run test script
python run_rag.py test
```

## 📁 File Description / 文件说明 / ファイル説明

| Filename / 文件名 / ファイル名 | Description / 说明 / 説明 |
|-------------------------------|---------------------------|
| `run_rag.py` | Main program file / 主程序文件 / メインプログラムファイル |
| `requirements_local.txt` | Dependency package list / 依赖包列表 / 依存関係パッケージリスト |
| `Meta-Llama-3.1-8B-Instruct-Q8_0.gguf` | LLM model file (~8GB) / LLM模型文件 / LLMモデルファイル |
| `public.txt` | Public test questions / 公开测试问题 / 公開テスト問題 |
| `private.txt` | Private test questions / 私有测试问题 / プライベートテスト問題 |

## ⚙️ Configuration Options / 配置选项 / 設定オプション

### CPU Thread Adjustment / CPU线程数调整 / CPUスレッド数調整
Modify in `run_rag.py`:
```python
llama3 = Llama(
    str(model_path),
    verbose=False,
    n_gpu_layers=0,  # Use CPU
    n_ctx=16384,     # Context window size
    n_threads=4,     # Adjust CPU threads (based on your CPU cores)
)
```

### Search Parameter Adjustment / 搜索参数调整 / 検索パラメータ調整
```python
# Adjust search strategies in the pipeline function
search_strategies = [
    f'"{keywords}"',  # Exact keyword match
    f'"{cleaned_question}"',  # Exact cleaned question match
    f'"{keywords}" 校歌',  # Keywords + school song
    keywords,  # Original keywords (backup)
]
```

## 🔧 Performance Optimization Tips / 性能优化建议 / パフォーマンス最適化のヒント

### 1. CPU Optimization / CPU优化 / CPU最適化
- **Thread Count**: Set to 1-2 times the number of CPU cores
- **Memory**: Ensure sufficient available memory
- **Cooling**: Pay attention to CPU cooling during long runs

### 2. Network Optimization / 网络优化 / ネットワーク最適化
- **Search Frequency**: Avoid too frequent search requests
- **Timeout Settings**: Appropriately adjust network request timeout
- **Proxy**: Use proxy server if needed

### 3. Storage Optimization / 存储优化 / ストレージ最適化
- **Model Files**: Ensure sufficient space for 8GB model file
- **Temporary Files**: Regularly clean generated temporary files

## 🐛 Common Issues / 常见问题 / よくある問題

### 1. Model Download Failure / 模型下载失败 / モデルダウンロード失敗
```bash
# Manually download model file
wget https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf
```

### 2. Dependency Package Installation Failure / 依赖包安装失败 / 依存関係パッケージインストール失敗
```bash
# Use domestic mirror source
pip install -r requirements_local.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 3. Insufficient Memory / 内存不足 / メモリ不足
- Reduce `n_threads` parameter
- Reduce `n_ctx` parameter
- Close other memory-consuming programs

### 4. Search Failure / 搜索失败 / 検索失敗
- Check network connection
- Wait a while and retry
- Consider using VPN or proxy

## 📊 Performance Benchmarks / 性能基准 / パフォーマンスベンチマーク

| Configuration / 配置 / 設定 | Inference Speed / 推理速度 / 推論速度 | Memory Usage / 内存使用 / メモリ使用量 | Recommended Scenarios / 推荐场景 / 推奨シナリオ |
|----------------------------|--------------------------------------|--------------------------------------|-----------------------------------------------|
| 4 threads | ~2-3s/question | ~4GB | Development testing |
| 8 threads | ~1-2s/question | ~6GB | Daily use |
| 16 threads | ~0.5-1s/question | ~8GB | Batch processing |

## 🎯 Usage Examples / 使用示例 / 使用例

### Single Question Test / 单个问题测试 / 単一問題テスト
```python
import asyncio
from run_rag import pipeline

async def test():
    question = "What is the school song of Guanghua Elementary School?"
    answer = await pipeline(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")

asyncio.run(test())
```

### Batch Processing / 批量处理 / バッチ処理
```python
import asyncio
from run_rag import main

# Process all questions
asyncio.run(main())
```

## 📝 Output Files / 输出文件 / 出力ファイル

After running, the following files will be generated:
- `local_cpu_test_1.txt` to `local_cpu_test_90.txt`: Answers for each question
- `local_cpu_test.txt`: All answers merged

## 🔄 Update Log / 更新日志 / 更新ログ

- **v1.0**: Initial version, supports local CPU operation
- **v1.1**: Added automatic dependency installation and file download
- **v1.2**: Optimized search strategies and error handling

## 📞 Technical Support / 技术支持 / テクニカルサポート

If you encounter problems, please check:
1. Python version is 3.8+
2. Sufficient disk space
3. Normal network connection
4. Adequate system memory

## ⚠️ Important Notes / 注意事项 / 重要な注意事項

1. **First Run**: Requires downloading 8GB model file, please be patient
2. **Web Search**: May be limited by Google search restrictions, use moderately
3. **CPU Usage**: Long runs will consume significant CPU resources
4. **File Permissions**: Ensure the program has read/write permissions for the current directory

---

## 📚 Academic Reference / 学术参考 / 学術参考

This implementation is based on the Machine Learning 2025 Spring course at National Taiwan University, specifically Homework 1: AI Agent1 -- RAG.

此实现基于台湾大学2025年春季机器学习课程，特别是作业1：AI Agent1 -- RAG。

この実装は、台湾大学2025年春学期機械学習コース、特に宿題1：AI Agent1 -- RAGに基づいています。

**Course Link**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)
**Instructor**: Prof. Hung-yi Lee (李宏毅教授)
**Course**: Machine Learning 2025 Spring
**Homework**: HW1 - AI Agent1 -- RAG 