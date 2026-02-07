#!/usr/bin/env python3
"""
Code Genie - AI offline per generazione di codice
"""

import argparse
from core.code_generator import CodeGenerator
from interface.cli import CLI

def main():
    parser = argparse.ArgumentParser(
        description='Code Genie - AI offline per generazione di script'
    )
    parser.add_argument(
        '--prompt', 
        type=str, 
        help='Descrizione dello script da generare'
    )
    parser.add_argument(
        '--language', 
        type=str, 
        default='python',
        help='Linguaggio di programmazione (default: python)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='deepseek-coder:6.7b',
        help='Modello da utilizzare (default: deepseek-coder:6.7b)'
    )
    
    args = parser.parse_args()
    
    # Inizializza il generatore
    generator = CodeGenerator(model=args.model)
    
    if args.prompt:
        # Modalità single-shot
        result = generator.generate(args.prompt, args.language)
        print(result)
    else:
        # Modalità interattiva
        cli = CLI(generator)
        cli.run()

if __name__ == '__main__':
    main()
