#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的RAG运行脚本 - 本地CPU版本
Simplified RAG runner - Local CPU Version
"""

import asyncio
import sys
from pathlib import Path

# 添加共享数据路径
SHARED_DATA_PATH = Path(__file__).parent.parent / "shared_data"

# 导入必要的库
from llama_cpp import Llama
from typing import List
from googlesearch import search as _search
from bs4 import BeautifulSoup
from charset_normalizer import detect
from requests_html import AsyncHTMLSession
import urllib3
urllib3.disable_warnings()

print("🚀 正在加载模型...")

# 加载模型到CPU - 使用共享数据路径
model_path = SHARED_DATA_PATH / "Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"
llama3 = Llama(
    str(model_path),
    verbose=False,
    n_gpu_layers=0,  # 使用CPU
    n_ctx=16384,     # 上下文窗口大小
    n_threads=4,     # CPU线程数，可以根据你的CPU调整
)

def generate_response(_model: Llama, _messages: str) -> str:
    '''
    这个函数将使用给定的消息对模型进行推理。
    '''
    _output = _model.create_chat_completion(
        _messages,
        stop=["<|eot_id|>", "<|end_of_text|>"],
        max_tokens=512,
        temperature=0,
        repeat_penalty=2.0,
    )["choices"][0]["message"]["content"]
    return _output

# 搜索工具
async def worker(s:AsyncHTMLSession, url:str):
    """异步获取网页内容"""
    try:
        header_response = await asyncio.wait_for(s.head(url, verify=False), timeout=10)
        if 'text/html' not in header_response.headers.get('Content-Type', ''):
            return None
        r = await asyncio.wait_for(s.get(url, verify=False), timeout=10)
        return r.text
    except:
        return None

async def get_htmls(urls):
    """异步获取多个网页的HTML内容"""
    session = AsyncHTMLSession()
    tasks = (worker(session, url) for url in urls)
    return await asyncio.gather(*tasks)

async def search(keyword: str, n_results: int=3) -> List[str]:
    '''
    搜索关键词并返回网页文本内容
    '''
    keyword = keyword[:100]
    results = list(_search(keyword, n_results * 2, lang="zh", unique=True))
    results = await get_htmls(results)
    results = [x for x in results if x is not None]
    results = [BeautifulSoup(x, 'html.parser') for x in results]
    results = [''.join(x.get_text().split()) for x in results if detect(x.encode()).get('encoding') == 'utf-8']
    return results[:n_results]

# Agent类
class LLMAgent():
    def __init__(self, role_description: str, task_description: str, llm:str="bartowski/Meta-Llama-3.1-8B-Instruct-GGUF"):
        self.role_description = role_description
        self.task_description = task_description
        self.llm = llm
    
    def inference(self, message:str) -> str:
        if self.llm == 'bartowski/Meta-Llama-3.1-8B-Instruct-GGUF':
            messages = [
                {"role": "system", "content": f"{self.role_description}"},
                {"role": "user", "content": f"{self.task_description}\n{message}"},
            ]
            return generate_response(llama3, messages)
        else:
            return ""

# 定义各个代理
question_extraction_agent = LLMAgent(
    role_description="你是一个专业的问题分析专家，擅长从复杂问题中提取核心内容。",
    task_description="请分析以下问题，提取核心问题内容，保持问题的核心含义。如果问题已经简洁明了，请直接返回原问题。",
)

keyword_extraction_agent = LLMAgent(
    role_description="你是一个专业的关键词提取专家，擅长从问题中识别最重要的搜索关键词。",
    task_description="请从以下问题中提取3-5个最重要的搜索关键词，用空格分隔。关键词应该能准确反映问题的核心内容，便于网络搜索找到相关信息。",
)

qa_agent = LLMAgent(
    role_description="你是 LLaMA-3.1-8B，是用來回答問題的 AI。",
    task_description="请根据你的知识库和提供的相关信息，全面、准确地回答以下问题。如果相关信息与问题相关，请充分利用；如果信息不足，请基于你的知识进行回答。直接输出最终答案的内容。不用输出中间的分析过程和不相关的信息。",
)

answer_verification_agent = LLMAgent(
    role_description="你是一个专业的答案检查专家。你的任务是对于被提出的问题，确保AI生成的答案是准确的,符合逻辑的。",
    task_description="请检查核对答案是否正确的符合逻辑的回答了被提出的问题，如果有错误请修正答案，并直接输出最终修正答案的内容，如果没有错误，直接输出最终答案的内容。不用输出中间的分析过程和不相关的信息。"
)

# RAG管道
async def pipeline(question: str) -> str:
    """
    4-Agent协作的RAG管道
    """
    try:
        # Step 1: 问题清理
        cleaned_question = question_extraction_agent.inference(question)
        print(f"清理后问题: {cleaned_question}")
        
        # Step 2: 关键词提取
        keywords = keyword_extraction_agent.inference(cleaned_question)
        print(f"提取关键词: {keywords}")

        # Step 3: 网络搜索
        try:
            search_strategies = [
                f'"{keywords}"',
                f'"{cleaned_question}"',
                f'"{keywords}" 校歌',
                keywords,
            ]
            
            search_results = []
            for strategy in search_strategies:
                try:
                    results = await search(strategy, n_results=2)
                    search_results.extend(results)
                    if len(search_results) >= 3:
                        break
                except Exception as e:
                    continue
            
            unique_results = list(dict.fromkeys(search_results))
            truncated_search_results = [result[:2000] for result in unique_results[:3]]
            
            if truncated_search_results:
                formatted_results = []
                for i, result in enumerate(truncated_search_results, 1):
                    cleaned_result = result.strip()
                    
                    if cleaned_result and len(cleaned_result) > 50:
                        import re
                        cleaned_result = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', cleaned_result)
                        cleaned_result = re.sub(r'\s+', ' ', cleaned_result)
                        cleaned_result = re.sub(r'<[^>]+>', '', cleaned_result)
                        cleaned_result = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', cleaned_result)
                        
                        if cleaned_result.strip() and len(cleaned_result.strip()) > 30:
                            formatted_results.append(f"参考信息{i}: {cleaned_result.strip()}")
                
                if formatted_results:
                    enhanced_question = f"问题：{cleaned_question}\n\n参考信息：\n" + "\n\n".join(formatted_results)
                else:
                    enhanced_question = cleaned_question
            else:
                enhanced_question = cleaned_question
        except Exception as e:
            print(f"搜索失败: {e}")
            enhanced_question = cleaned_question
        
        if "参考信息" not in enhanced_question:
            print("未找到相关参考信息，使用LLM知识库回答")
            enhanced_question = f"问题：{cleaned_question}\n\n请基于你的知识库回答这个问题，不需要外部参考信息。"

        # Step 4: 生成初步答案
        initial_answer = qa_agent.inference(enhanced_question)
        print(f"初步答案: {initial_answer}")

        # Step 5: 答案质量检查
        final_answer = answer_verification_agent.inference(initial_answer)
        print(f"最终答案: {final_answer}")

        return final_answer
        
    except Exception as e:
        print(f"管道执行失败: {e}")
        return qa_agent.inference(question)

# 测试函数
async def test_single_question():
    """测试单个问题"""
    print("🧪 测试单个问题...")
    print("=" * 50)
    
    test_question = "光華國小的校歌是『虎山雄風飛揚』。"
    print(f"测试问题: {test_question}")
    print("-" * 30)
    
    try:
        answer = await pipeline(test_question)
        print(f"生成的答案: {answer}")
        print(f"答案长度: {len(answer)} 字符")
        
        if answer and len(answer.strip()) > 0:
            print("✅ 测试成功！pipeline函数正常工作")
        else:
            print("❌ 测试失败！pipeline函数没有生成答案")
            
    except Exception as e:
        print(f"❌ 测试失败！错误: {e}")
        import traceback
        traceback.print_exc()
    
    print("=" * 50)

# 主函数
async def main():
    """主函数"""
    print("🎯 开始处理问题...")
    
    STUDENT_ID = "local_cpu_test"
    
    # 处理public.txt中的问题 - 使用共享数据路径
    public_path = SHARED_DATA_PATH / "public.txt"
    if public_path.exists():
        print("📖 处理public.txt中的问题...")
        with open(public_path, 'r', encoding='utf-8') as input_f:
            questions = input_f.readlines()
            questions = [l.strip().split(',')[0] for l in questions]
            
            for id, question in enumerate(questions, 1):
                output_path = Path(f"./{STUDENT_ID}_{id}.txt")
                if output_path.exists():
                    print(f"跳过问题 {id} (已存在)")
                    continue
                
                print(f"\n处理问题 {id}: {question}")
                answer = await pipeline(question)
                answer = answer.replace('\n',' ')
                print(f"答案: {answer}")
                
                with open(output_path, 'w', encoding='utf-8') as output_f:
                    print(answer, file=output_f)
    
    # 处理private.txt中的问题 - 使用共享数据路径
    private_path = SHARED_DATA_PATH / "private.txt"
    if private_path.exists():
        print("📖 处理private.txt中的问题...")
        with open(private_path, 'r', encoding='utf-8') as input_f:
            questions = input_f.readlines()
            
            for id, question in enumerate(questions, 31):
                output_path = Path(f"./{STUDENT_ID}_{id}.txt")
                if output_path.exists():
                    print(f"跳过问题 {id} (已存在)")
                    continue
                
                print(f"\n处理问题 {id}: {question}")
                answer = await pipeline(question)
                answer = answer.replace('\n',' ')
                print(f"答案: {answer}")
                
                with open(output_path, 'w', encoding='utf-8') as output_f:
                    print(answer, file=output_f)
    
    # 合并结果到一个文件
    print("📝 合并结果...")
    with open(f'./{STUDENT_ID}.txt', 'w', encoding='utf-8') as output_f:
        for id in range(1, 91):
            file_path = Path(f'./{STUDENT_ID}_{id}.txt')
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as input_f:
                    answer = input_f.readline().strip()
                    print(answer, file=output_f)
            else:
                print("", file=output_f)
    
    print("✅ 处理完成！")

if __name__ == "__main__":
    print("🚀 启动本地CPU版本的RAG系统...")
    
    # 选择运行模式
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        asyncio.run(test_single_question())
    else:
        asyncio.run(main()) 