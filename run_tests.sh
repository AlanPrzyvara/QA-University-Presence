#!/bin/bash

# Script para executar os testes automatizados
# Uso: ./run_tests.sh [opções]

echo "🚀 Iniciando testes automatizados de login..."
echo ""

# Verifica se o servidor está rodando
if ! curl -s http://localhost:3001 > /dev/null 2>&1; then
    echo "⚠️  AVISO: Não foi possível conectar ao servidor em http://localhost:3001"
    echo "   Certifique-se de que o servidor está rodando antes de executar os testes."
    echo ""
fi

# Executa os testes
if [ "$1" == "--html" ]; then
    echo "📊 Executando testes com relatório HTML..."
    pytest tests/ --html=report.html --self-contained-html
elif [ "$1" == "--verbose" ] || [ "$1" == "-v" ]; then
    echo "📝 Executando testes em modo verbose..."
    pytest tests/ -v
elif [ "$1" == "--validation" ]; then
    echo "✅ Executando apenas testes de validação..."
    pytest tests/test_login.py -k "validacao" -v
elif [ "$1" == "--negative" ]; then
    echo "❌ Executando apenas testes de cenários negativos..."
    pytest tests/test_login.py -k "falha" -v
else
    echo "🧪 Executando todos os testes..."
    pytest tests/ -v
fi

echo ""
echo "✅ Testes concluídos!"

