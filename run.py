#!/usr/bin/env python3
"""
Script para executar o Sistema de Gestão Pessoal
"""

import uvicorn
import os
import sys

def main():
    """Executar a aplicação"""
    print("🚀 Iniciando Sistema de Gestão Pessoal...")
    print("📊 Frontend: Abra 'controle de dados.html' no navegador")
    print("🔗 API Docs: http://localhost:8000/docs")
    print("📖 ReDoc: http://localhost:8000/redoc")
    print("🛑 Para parar: Ctrl+C")
    print("-" * 50)
    
    try:
        uvicorn.run(
            "backend.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Sistema finalizado!")
        sys.exit(0)

if __name__ == "__main__":
    main()