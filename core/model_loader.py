"""
Gestisce il caricamento e l'interazione con i modelli Ollama
"""

import ollama
import yaml
import os
from typing import Optional

class ModelLoader:
    def __init__(self, model_name: Optional[str] = None):
        # Carichiamo la configurazione dallo YAML per non avere dati cablati
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'model_config.yaml')
        
        try:
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️ Errore caricamento config: {e}")
            self.config = {}

        # Priorità: 1. Argomento passato | 2. Default da YAML | 3. Hardcoded fallback
        self.model_name = model_name or self.config.get('default_model', "dolphin-llama3")
        self.client = ollama.Client()
        
    def is_model_available(self) -> bool:
        """Verifica se il modello è già scaricato"""
        try:
            response = self.client.list()
            # Gestione robusta per i diversi formati di risposta di Ollama
            model_list = response.get('models', [])
            return any(self.model_name in m.get('name', '') for m in model_list)
        except Exception as e:
            print(f"❌ Errore connessione Ollama: {e}")
            return False
    
    def pull_model(self):
        """Scarica il modello se non presente"""
        if not self.is_model_available():
            print(f"📥 Modello {self.model_name} non trovato. Download in corso...")
            try:
                self.client.pull(self.model_name)
                print("✅ Download completato!")
            except Exception as e:
                print(f"❌ Errore durante il download: {e}")
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Genera una risposta dal modello con i parametri dello YAML"""
        messages = []
        
        if system_prompt:
            messages.append({
                'role': 'system',
                'content': system_prompt
            })
        
        messages.append({
            'role': 'user',
            'content': prompt
        })
        
        # Recuperiamo i parametri di generazione dallo YAML
        gen_config = self.config.get('generation', {})
        
        response = self.client.chat(
            model=self.model_name,
            messages=messages,
            options={
                'temperature': gen_config.get('temperature', 0.1),
                'top_p': gen_config.get('top_p', 0.9),
                'num_predict': gen_config.get('max_tokens', 2048),
            }
        )
        
        return response['message']['content']
