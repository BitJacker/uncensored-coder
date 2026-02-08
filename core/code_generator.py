import os
import re
import logging
from typing import Optional, Dict, Any
from enum import Enum
from .model_loader import ModelLoader
from .prompt_templates import PromptTemplates

class SupportedLanguage(Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    CPP = "cpp"
    RUST = "rust"
    GO = "go"
    HTML = "html"
    CSS = "css"
    SQL = "sql"

class CodeGenerator:
    def __init__(self, model: str = "deepseek-coder:6.7b", enable_logging: bool = True):
        self.model_name = model
        self.logger = self._setup_logger(enable_logging)
        try:
            self.loader = ModelLoader(model)
            self.templates = PromptTemplates()
        except Exception as e:
            raise RuntimeError(f"Initialization Error: {e}")

    def _setup_logger(self, enable: bool):
        logger = logging.getLogger(__name__)
        if enable and not logger.handlers:
            h = logging.StreamHandler()
            h.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            logger.addHandler(h)
            logger.setLevel(logging.INFO)
        return logger

    def _clean_code(self, text: str) -> str:
        """Removes markdown blocks ``` and returns raw code only"""
        pattern = r"```(?:\w+)?\n(.*?)\n```"
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else text.strip()

    def generate(self, user_request: str, language: str = "python") -> str:
        # Optimization: We use English templates for global compatibility
        system_p = self.templates.get_system_prompt(language)
        user_p = self.templates.get_user_prompt(user_request, language)
        
        full_prompt = f"{system_p}\n\n{user_p}"
        raw_code = self.loader.generate(full_prompt)
        return self._clean_code(raw_code)

    def save_to_file(self, code: str, filename: str) -> str:
        os.makedirs("generated_code", exist_ok=True)
        path = os.path.join("generated_code", filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        return path
