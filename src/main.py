"""
GEO Visual Opportunity Engine - Main Entry Point
Author: Tim (sales@dageno.ai)
Version: 2.0.0

This module provides the main interface for the GEO Visual Opportunity Engine
with automatic Nano Banana 2 image generation.
"""

import os
import json
import sys
from typing import Dict, List, Optional, Any
from pathlib import Path

from .analyzer import OpportunityAnalyzer
from .nano_banana_2 import NanoBanana2, generate_images_from_prompts
from .config import AUTHOR_INFO, SKILL_CONFIG, validate_api_key


class GEOVisualEngine:
    """
    Main Engine for GEO Visual Opportunity Analysis
    with automatic image generation using Nano Banana 2
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the GEO Visual Engine

        Args:
            api_key: Google API Key for Nano Banana 2 (optional)
        """
        self.analyzer = OpportunityAnalyzer()
        self.image_generator = NanoBanana2(api_key=api_key)
        self.author_info = AUTHOR_INFO

        print(f"[INFO] GEO Visual Opportunity Engine v{SKILL_CONFIG['version']}")
        print(f"[AUTHOR] {self.author_info['name']} - {self.author_info['email']}")
        print(f"[WEBSITE] {self.author_info['website']}")

    def run(
        self,
        brand: str,
        product: str,
        core_keyword: str,
        country: str,
        language: str = "en",
        competitors: Optional[List[str]] = None,
        platform_focus: Optional[List[str]] = None,
        generate_images: bool = True
    ) -> Dict[str, Any]:
        """
        Run the complete GEO opportunity analysis with image generation

        Args:
            brand: Brand name
            product: Product name
            core_keyword: Core keyword/phrase
            country: Target country code (e.g., "us", "uk")
            language: Output language code (e.g., "en", "zh")
            competitors: List of competitor brands
            platform_focus: Target AI platforms
            generate_images: Whether to generate images (default: True)

        Returns:
            Complete result dictionary with opportunities, prompts, images, and schedule
        """
        print(f"\n[STEP 1] Analyzing: {brand} - {product}")
        print(f"[KEYWORD] {core_keyword}")
        print(f"[TARGET] {country} / {language}")

        # Step 1: Analyze opportunities
        print("\n[STEP 2] Generating opportunities and prompts...")
        analysis_result = self.analyzer.analyze(
            brand=brand,
            product=product,
            core_keyword=core_keyword,
            country=country,
            language=language,
            competitors=competitors,
            platform_focus=platform_focus
        )

        print(f"[FOUND] {len(analysis_result['opportunities'])} opportunities")

        # Step 2: Generate images if requested
        generated_images = []

        if generate_images:
            print("\n[STEP 3] Invoking Nano Banana 2 (Model: gemini-3.1-flash-image)...")

            # Check API key
            if not validate_api_key():
                print("[WARNING] No Google API Key found. Images will be simulated.")

            # Generate images for each opportunity
            for prompt_group in analysis_result["image_prompts"]:
                opportunity_id = prompt_group["opportunity_id"]

                # Prepare prompts for batch generation
                prompts_to_generate = []
                for style in ["white_info", "lifestyle", "hero"]:
                    if style in prompt_group:
                        prompts_to_generate.append({
                            "style": style,
                            "prompt": prompt_group[style]["prompt"]
                        })

                # Generate batch
                results = self.image_generator.generate_batch(
                    prompts_to_generate,
                    opportunity_id
                )

                generated_images.extend(results)

            print(f"[SUCCESS] Generated {len(generated_images)} images")

        # Add generated images to result
        analysis_result["generated_images"] = generated_images

        return analysis_result

    def save_result(self, result: Dict, output_path: str = "output/result.json") -> None:
        """
        Save result to JSON file

        Args:
            result: Result dictionary
            output_path: Output file path
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"[SAVED] Result saved to {output_path}")


def main():
    """
    Main function for command-line usage
    """
    # Example usage
    engine = GEOVisualEngine()

    # Run analysis with sample data
    result = engine.run(
        brand="AcmeWatch",
        product="Acme DivePro 5",
        core_keyword="smartwatch water resistance",
        country="us",
        language="en",
        competitors=["BrandA", "BrandB"],
        generate_images=True
    )

    # Save result
    engine.save_result(result, "output/analysis_result.json")

    print("\n[DONE] Analysis complete!")
    print(f"[RESULT] {len(result['opportunities'])} opportunities generated")
    print(f"[IMAGES] {len(result.get('generated_images', []))} images created")


if __name__ == "__main__":
    main()
