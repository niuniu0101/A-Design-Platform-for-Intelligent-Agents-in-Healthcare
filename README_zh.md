当然可以！以下是你提供的 GitHub 项目 README 的**中文版**，你可以保存为 `README_zh.md`：

------

### ![由 DeepSeek 驱动](https://img.shields.io/badge/Powered_by-DeepSeek_V3-0A0A0A?style=for-the-badge&logo=deepseek)

# 🩺面向医疗领域的智能体设计平台🩺

本项目是一个基于 [AgentOS](https://github.com/QinbinLi/AgentOS) 和 [together.ai（DeepSeek V3）](https://docs.together.ai/docs/serverless-models) 构建的体检推荐系统。它使用 RAG（检索增强生成）技术，根据用户信息推荐个性化体检套餐。

------

### 🗂️文件结构🗂️

```
A-Design-Platform-for-Intelligent-Agents-in-Healthcare/
├── config/
│   └── settings.py
├── data/
│   ├── health_check_data.csv
│   └── symptoms.pdf
├── agentos/
│   ├── agent/
│   ├── memory/
│   ├── prompt/
│   ├── rag/
│   ├── tools/
│   └── utils/
├── vectordb/
│   ├── vector_db_1/
│   └── vector_db_2/
├── src/
│   ├── vectorstore.py
│   ├── hcr.py
│   ├── hcr_prompts.py
│   ├── tools.py
│   └── utils.py
├── test/
├── web/
│   ├── pages/
│   │   ├── 1_🥰_Recommend.py
│   │   ├── 2_🤖_Chatbot.py
│   │   └── 3_🏥_Hospitals.py
│   └── 🩺HCR-HOME.py
├── requirements.txt
└── README.md
```

------

### 🚀运行方式🚀

1. 安装依赖：

```bash
pip install -r requirements.txt
```

1. 构建向量数据库：

```bash
python vectordb/vectorstore.py
```

1. 运行 Streamlit 应用：

```bash
streamlit run web/🩺HCR-HOME.py
```

------

### 💻技术栈💻

| 组件         | 所用技术              |
| ------------ | --------------------- |
| 大模型       | DeepSeek V3 API       |
| 智能体框架   | AgentOS               |
| 向量数据库   | Chromadb              |
| 前端界面     | Streamlit             |
| 文本嵌入模型 | BAAI/bge-base-zh      |
| 交叉编码器   | ms-marco-MiniLM-L6-v2 |

