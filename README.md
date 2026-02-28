# GEO Visual Opportunity Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.0.0-blue.svg)](https://github.com/GEO-SEO/geo-visual-opportunity-engine)
[![Platform](https://img.shields.io/badge/Platform-Dify%20%7C%20Coze%20%7C%20Python-orange.svg)](#)
[![Nano Banana 2](https://img.shields.io/badge/Powered%20By-Nano%20Banana%202-yellow.svg)](#)

> After inputting brand/product/keywords/competitors and target language, automatically outputs: priority opportunity list, content objectives, three sets of Nano-ready image prompts, **automatically generates images using Nano Banana 2 (Google Gemini)**, and provides a 4-week posting rhythm for brand GEO content pipeline production.

## Features

- **Smart Opportunity Analysis**: Identifies high-priority GEO opportunities based on brand, product, and core keywords
- **Three Image Prompts**: Generates white info, lifestyle, and hero image prompts for each opportunity
- **Auto Image Generation**: Automatically calls Nano Banana 2 (Google Gemini 3.1 Flash) to generate actual images
- **Localized Content**: Supports 10+ languages for content generation
- **4-Week Publishing Rhythm**: Provides complete content publishing plan with KPI suggestions
- **Structured Output**: Strict JSON format output for programmatic processing

## Quick Start

### Prerequisites

- Python 3.9+
- Google AI Studio API Key (for Nano Banana 2 image generation)

### Installation

```bash
# Clone the repository
git clone https://github.com/GEO-SEO/geo-visual-opportunity-engine.git
cd geo-visual-opportunity-engine

# Install dependencies
pip install -r requirements.txt

# Set your Google API Key
export GOOGLE_API_KEY="your-api-key-here"
```

### Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `brand` | string | Yes | Brand name |
| `product` | string | Yes | Product name |
| `core_keyword` | string | Yes | Core keyword |
| `country` | string | Yes | Target country code (e.g., us, uk, jp) |
| `language` | string | Yes | Output language code (e.g., en, zh, ja) |
| `competitors` | array | No | Competitor list (max 10) |
| `platform_focus` | array | No | Target AI platforms |

### Example Input

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

## Python Usage

```python
from src.main import GEOVisualEngine

# Initialize the engine
engine = GEOVisualEngine(api_key="your-google-api-key")

# Run analysis with auto image generation
result = engine.run(
    brand="AcmeWatch",
    product="Acme DivePro 5",
    core_keyword="smartwatch water resistance",
    country="us",
    language="en",
    competitors=["BrandA", "BrandB"]
)

# Result contains:
# - opportunities: List of GEO opportunities
# - image_prompts: Generated prompts for each opportunity
# - generated_images: Paths to Nano Banana 2 generated images
# - content_drafts: Localized content drafts
# - posting_schedule: 4-week publishing plan
```

## Platform Integration

### Dify.ai

1. Open Dify dashboard
2. Create new app or import existing
3. Copy `prompts/system_prompt.md` content to "Prompt" section
4. Configure input variables (reference `schemas/input_schema.json`)
5. Set output format to JSON

### Coze / GPTs

1. Create new Bot
2. Paste `prompts/system_prompt.md` as system prompt
3. Configure input form (reference field definitions in `schemas/input_schema.json`)
4. Set output format to JSON

### LangChain

```python
from langchain.prompts import PromptTemplate

with open('prompts/system_prompt.md', 'r') as f:
    system_prompt = f.read()

template = PromptTemplate(
    input_variables=["brand", "product", "core_keyword", "country", "language", "competitors", "platform_focus"],
    template=system_prompt
)
```

## Nano Banana 2 Integration

This skill automatically generates images using **Nano Banana 2** (Google Gemini 3.1 Flash Image) after creating the prompts.

### Image Styles

- **White Info**: Clean white background, infographic style, product-focused
- **Lifestyle**: Real-world场景, human interaction, photorealistic
- **Hero**: Dramatic lighting, commercial photography, brand impact

### Configuration

Set your Google API Key:

```bash
export GOOGLE_API_KEY="your-google-api-key"
```

Get your API key from: https://aistudio.google.com/app/apikey

## Project Structure

```
geo-visual-opportunity-engine/
├── manifest.json                 # Skill metadata
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── src/
│   ├── __init__.py
│   ├── main.py                  # Main entry point
│   ├── analyzer.py              # Opportunity analysis
│   ├── nano_banana_2.py         # Nano Banana 2 image generation
│   └── config.py                # Configuration
├── schemas/
│   ├── input_schema.json        # Input JSON Schema
│   └── output_schema.json       # Output JSON Schema
├── prompts/
│   └── system_prompt.md         # Core system prompt
└── examples/
    ├── example_input.json       # Example input
    └── example_output.json      # Example output
```

## Output Format

### Success Response

```json
{
  "opportunities": [...],
  "image_prompts": [...],
  "generated_images": [...],
  "content_drafts": [...],
  "posting_schedule": {...},
  "meta": {...}
}
```

### Error Response

```json
{
  "error": "invalid_input",
  "details": "Required field cannot be empty"
}
```

## Supported Languages

- English
- Chinese
- Japanese
- Spanish
- French
- German
- Korean
- Portuguese
- Italian
- Russian

## Version History

### v2.0.0 (2026-02-28)

- Added automatic Nano Banana 2 image generation
- Upgraded to Google Gemini 3.1 Flash Image model
- Added Python SDK for local execution
- All documentation in English

### v1.0.0 (2025-03-10)

- Initial release
- Structured JSON input/output
- Three-image prompt generation
- 4-week publishing rhythm planning

## Contributing

Issues and Pull Requests are welcome!

1. Fork this repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add some amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Author

- **Tim**
- Email: sales@dageno.ai
- Website: https://dageno.ai/

---

*This skill helps brand marketing teams quickly generate GEO-optimized content and visual assets, improving brand visibility in AI search engines.*
