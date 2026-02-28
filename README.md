# GEO 视觉机会工厂

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/your-username/geo-visual-opportunity-engine)
[![Platform](https://img.shields.io/badge/Platform-Dify%20%7C%20Coze%20%7C%20LangChain-orange.svg)](#)

> 输入品牌/产品/关键词/竞品与目标语言后，自动输出优先级机会清单、每个机会的内容目标、三套 Nano-ready 图像 prompt、文案稿与 4 周发布节奏。用于品牌的 GEO 内容流水线化生产。

## 功能特性

- **智能机会分析**：基于品牌、产品和核心关键词，识别高优先级的 GEO 机会点
- **三套图像 Prompt**：为每个机会生成白底信息图、场景图、封面图三种类型的 AI 图像提示词
- **本地化内容**：支持 10+ 种语言的本地化内容生成
- **四周发布节奏**：提供完整的内容发布计划和 KPI 建议
- **结构化输出**：严格的 JSON 格式输出，便于程序化处理

## 快速开始

### 输入参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `brand` | string | 是 | 品牌名称 |
| `product` | string | 是 | 产品名称 |
| `core_keyword` | string | 是 | 核心关键词 |
| `country` | string | 是 | 目标国家代码（如 us, uk, jp） |
| `language` | string | 是 | 输出语言代码（如 en, zh, ja） |
| `competitors` | array | 否 | 竞争对手列表（最多 10 个） |
| `platform_focus` | array | 否 | 目标 AI 平台 |

### 示例输入

```json
{
  "brand": "AcmeWatch",
  "product": "Acme DivePro 5",
  "core_keyword": "smartwatch water resistance",
  "country": "us",
  "language": "en",
  "competitors": ["BrandA", "BrandB"],
  "platform_focus": ["ChatGPT", "Grok"]
}
```

### 平台集成

#### Dify.ai

1. 打开 Dify 工作台
2. 创建新应用或导入现有应用
3. 在「提示词」部分，复制 `prompts/system_prompt.md` 的内容
4. 配置输入变量（参考 `schemas/input_schema.json`）
5. 配置输出格式为 JSON

#### Coze / GPTs

1. 创建新 Bot
2. 在系统提示词中粘贴 `prompts/system_prompt.md` 的内容
3. 配置输入表单（参考 `schemas/input_schema.json` 中的字段定义）
4. 设置输出格式为 JSON

#### LangChain

```python
from langchain.prompts import PromptTemplate

with open('prompts/system_prompt.md', 'r') as f:
    system_prompt = f.read()

template = PromptTemplate(
    input_variables=["brand", "product", "core_keyword", "country", "language", "competitors", "platform_focus"],
    template=system_prompt
)
```

## 项目结构

```
geo-visual-opportunity-engine/
├── manifest.json                 # Skill 元数据配置
├── README.md                     # 项目说明文档
├── LICENSE                       # 开源许可证
├── schemas/
│   ├── input_schema.json         # 输入参数 JSON Schema
│   └── output_schema.json        # 输出结构 JSON Schema
├── prompts/
│   └── system_prompt.md          # 核心系统提示词
└── examples/
    ├── example_input.json        # 示例输入
    └── example_output.json       # 示例输出
```

## 输出格式

### 成功响应

```json
{
  "opportunities": [...],
  "image_prompts": [...],
  "content_drafts": [...],
  "posting_schedule": {...},
  "meta": {...}
}
```

### 错误响应

```json
{
  "error": "invalid_input",
  "details": "必填字段不能为空"
}
```

## 支持的语言

- 英语 (English)
- 中文 (Chinese)
- 日语 (Japanese)
- 西班牙语 (Spanish)
- 法语 (French)
- 德语 (German)
- 韩语 (Korean)
- 葡萄牙语 (Portuguese)
- 意大利语 (Italian)
- 俄语 (Russian)

## 版本历史

### v1.0.0 (2025-03-10)

- 初始版本发布
- 支持结构化输入和 JSON 输出
- 提供三套图像 prompt 生成
- 包含四周发布节奏规划

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 作者：Your Name
- 邮箱：your.email@example.com
- 网站：https://your-website.com

---

*本 Skill 旨在帮助品牌营销团队快速生成 GEO 优化内容，提升品牌在 AI 搜索引擎中的可见度。*
