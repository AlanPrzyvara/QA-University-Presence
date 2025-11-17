# Testes Automatizados - Tela de Login

Este projeto contém testes automatizados usando Selenium WebDriver para validar a funcionalidade de login da aplicação.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chrome/Chromium instalado no sistema
- Servidor da aplicação rodando em `http://localhost:3001`

## 🚀 Instalação

1. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🧪 Executando os Testes

### Executar todos os testes

```bash
pytest tests/
```

### Executar um teste específico

```bash
pytest tests/test_login.py::TestLogin::test_login_sucesso_credenciais_validas
```

### Executar com relatório HTML

```bash
pytest tests/ --html=report.html --self-contained-html
```

### Executar em modo verbose (mostra mais detalhes)

```bash
pytest tests/ -v
```

### Executar apenas testes de validação

```bash
pytest tests/test_login.py -k "validacao"
```

### Executar apenas testes de cenários negativos

```bash
pytest tests/test_login.py -k "falha"
```

## 📝 Estrutura dos Testes

### Cenários Positivos
- ✅ Login bem-sucedido com credenciais válidas

### Cenários Negativos
- ❌ Login falha com email inválido
- ❌ Login falha com senha incorreta
- ❌ Login falha com credenciais incorretas
- ❌ Login falha com formato de email inválido

### Validações de Campos Obrigatórios
- ⚠️ Validação de campo email obrigatório
- ⚠️ Validação de campo senha obrigatório
- ⚠️ Validação de ambos os campos obrigatórios

### Cenários Adicionais
- 🔄 Limpar campos após preenchimento

## 🔧 Configuração

### Credenciais Válidas

As credenciais válidas estão configuradas no arquivo `tests/conftest.py`:

- **Email**: `test@universitypresence.com`
- **Senha**: `123456`

### Seletores dos Elementos

- **Campo Email**: `id="email"`
- **Campo Senha**: `id="password"`
- **Botão Entrar**: `type="submit"`

### Modo Headless

Para executar os testes sem interface gráfica (útil para CI/CD), descomente a linha no arquivo `tests/conftest.py`:

```python
chrome_options.add_argument("--headless")
```

## 📊 Relatórios

Os relatórios HTML são gerados automaticamente quando você usa a flag `--html`. Abra o arquivo `report.html` no navegador para visualizar os resultados detalhados.

## 🐛 Troubleshooting

### Erro: ChromeDriver não encontrado
O projeto usa `webdriver-manager` que baixa automaticamente o ChromeDriver. Se houver problemas:

1. **No Linux/WSL**: Instale o Chrome/Chromium:
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install -y google-chrome-stable
   # ou
   sudo apt-get install -y chromium-browser
   ```

2. **Usar ChromeDriver local**: Coloque o `chromedriver` (Linux) ou `chromedriver.exe` (Windows) no diretório raiz do projeto.

3. **Definir variável de ambiente**:
   ```bash
   export CHROMEDRIVER_PATH=/caminho/para/chromedriver
   ```

### Erro: `AttributeError: 'NoneType' object has no attribute 'split'`
Este erro ocorre quando o `webdriver-manager` não consegue detectar a versão do Chrome. Soluções:

1. Instale o Chrome/Chromium no sistema (veja acima)
2. Use um ChromeDriver local no diretório do projeto
3. Defina `CHROMEDRIVER_PATH` apontando para o executável

### Erro: Timeout ao conectar
Certifique-se de que o servidor está rodando em `http://localhost:3001` antes de executar os testes.

### Erro: Elemento não encontrado
Verifique se os IDs dos elementos na aplicação correspondem aos esperados:
- `id="email"`
- `id="password"`
- `button[type="submit"]`

### Erro: Permissão negada (Linux/WSL)
Se o ChromeDriver não for executável:
```bash
chmod +x chromedriver
```

## 📚 Estrutura do Projeto

```
qauniversitypresence/
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Configuração e fixtures
│   └── test_login.py        # Testes de login
├── requirements.txt          # Dependências Python
└── README.md                # Este arquivo
```

## 🔍 Boas Práticas Implementadas

- ✅ Separação de responsabilidades (Page Object Pattern parcial)
- ✅ Fixtures reutilizáveis para WebDriver
- ✅ Testes independentes e isolados
- ✅ Seletores centralizados
- ✅ Documentação clara de cada teste
- ✅ Tratamento de timeouts e exceções
- ✅ Suporte a validações HTML5 e JavaScript

