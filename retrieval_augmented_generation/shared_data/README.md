# Shared Data Directory / 共享数据目录 / 共有データディレクトリ

## 📁 Required Files / 必需文件 / 必要なファイル

This directory should contain the following files for the RAG system to work properly:

此目录应包含以下文件以使RAG系统正常工作：

このディレクトリには、RAGシステムが正常に動作するために以下のファイルが含まれている必要があります：

### 1. Model File / 模型文件 / モデルファイル
- **File**: `Meta-Llama-3.1-8B-Instruct-Q8_0.gguf`
- **Size**: ~8GB
- **Download**: Automatically downloaded when running the system for the first time

### 2. Test Data Files / 测试数据文件 / テストデータファイル
- **File**: `public.txt` - Public test questions
- **File**: `private.txt` - Private test questions

## 🚀 Automatic Download / 自动下载 / 自動ダウンロード

The system will automatically download these files when you run it for the first time:

系统在首次运行时会自动下载这些文件：

システムは初回実行時にこれらのファイルを自動的にダウンロードします：

```bash
cd retrieval_augmented_generation
python3 start_local.py
```

## 📥 Manual Download / 手动下载 / 手動ダウンロード

If automatic download fails, you can manually download the files:

如果自动下载失败，您可以手动下载文件：

自動ダウンロードが失敗した場合、ファイルを手動でダウンロードできます：

### Model File / 模型文件 / モデルファイル
```bash
# Download the model file
wget https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf
```

### Test Data / 测试数据 / テストデータ
The test data files (`public.txt` and `private.txt`) contain sample questions for testing the RAG system.

测试数据文件（`public.txt` 和 `private.txt`）包含用于测试RAG系统的示例问题。

テストデータファイル（`public.txt` と `private.txt`）には、RAGシステムをテストするためのサンプル質問が含まれています。

## ⚠️ Important Notes / 重要说明 / 重要な注意事項

1. **Large File**: The model file is approximately 8GB in size
2. **Download Time**: May take 10-30 minutes depending on your internet connection
3. **Storage Space**: Ensure you have at least 10GB of free space
4. **Network**: Stable internet connection required for download

## 🔧 Troubleshooting / 故障排除 / トラブルシューティング

If you encounter download issues:

如果遇到下载问题：

ダウンロードの問題が発生した場合：

1. **Check Network**: Ensure stable internet connection
2. **Retry**: The system supports resume download
3. **Manual Download**: Use the manual download commands above
4. **Proxy/VPN**: Consider using proxy or VPN if needed

---

**Reference Course**: [Machine Learning 2025 Spring - NTU](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php) 