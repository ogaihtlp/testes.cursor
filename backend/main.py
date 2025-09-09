from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel
from .database import engine, create_db_and_tables
from .routers import monthly, travel, stats

# Criar aplicação FastAPI
app = FastAPI(
    title="Sistema de Gestão Pessoal API",
    description="API para gerenciar dados mensais e registros de viagem",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Eventos de inicialização
@app.on_event("startup")
def on_startup():
    """Criar tabelas no banco de dados na inicialização"""
    create_db_and_tables()
    print("🚀 API do Sistema de Gestão Pessoal iniciada!")
    print("📊 Acesse a documentação em: http://localhost:8000/docs")

@app.on_event("shutdown")
def on_shutdown():
    """Cleanup na finalização da aplicação"""
    print("👋 API do Sistema de Gestão Pessoal finalizada!")

# Rotas principais
@app.get("/")
def root():
    """Endpoint raiz da API"""
    return {
        "ok": True,
        "service": "gestao-pessoal-api",
        "version": "1.0.0",
        "message": "Sistema de Gestão Pessoal - API funcionando!"
    }

@app.get("/health")
def health():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "service": "gestao-pessoal-api"
    }

# Incluir routers
app.include_router(monthly.router, prefix="/api/monthly", tags=["Dados Mensais"]) 
app.include_router(travel.router, prefix="/api/travel", tags=["Registros de Viagem"])
app.include_router(stats.router, prefix="/api/stats", tags=["Estatísticas"])

# Servir arquivos estáticos (opcional)
try:
    app.mount("/static", StaticFiles(directory="../"), name="static")
except Exception:
    pass  # Diretório static não existe

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )