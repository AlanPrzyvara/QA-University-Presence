"""
Configuração base para os testes Selenium.
Define fixtures compartilhadas e configuração do WebDriver.
"""
import os
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_chromedriver_path():
    """
    Retorna o caminho do ChromeDriver.
    Prioriza chromedriver local, depois tenta webdriver-manager.
    """
    import platform
    
    project_root = Path(__file__).parent.parent
    system = platform.system().lower()
    
    # Verifica se há chromedriver no diretório do projeto
    # No Linux/WSL, procura por 'chromedriver' (sem extensão)
    # No Windows, procura por 'chromedriver.exe'
    if system == "windows":
        local_chromedriver = project_root / "chromedriver.exe"
    else:
        local_chromedriver = project_root / "chromedriver"
    
    if local_chromedriver.exists() and os.access(local_chromedriver, os.X_OK):
        return str(local_chromedriver.absolute())
    
    # Tenta usar webdriver-manager com tratamento de erro melhorado
    try:
        # Tenta instalar sem detectar versão do Chrome (mais robusto)
        # Isso evita o erro 'NoneType' object has no attribute 'split'
        # Usa cache_version para evitar detecção automática problemática
        import os as os_module
        os_module.environ['WDM_LOG_LEVEL'] = '0'  # Desabilita logs verbosos
        
        driver_path = ChromeDriverManager().install()
        if driver_path and os.path.exists(driver_path):
            # Torna executável no Linux
            if system != "windows":
                os.chmod(driver_path, 0o755)
            return driver_path
    except (AttributeError, TypeError, ValueError) as e:
        # Erro comum: webdriver-manager não consegue detectar versão do Chrome
        # Tenta usar uma versão específica conhecida
        try:
            # Tenta baixar versão mais recente disponível sem detectar Chrome
            driver_path = ChromeDriverManager(version="latest").install()
            if driver_path and os.path.exists(driver_path):
                if system != "windows":
                    os.chmod(driver_path, 0o755)
                return driver_path
        except Exception as inner_e:
            # Se ainda falhar, continua para outras tentativas
            pass
    except Exception as e:
        # Se falhar, tenta usar chromedriver do PATH ou variável de ambiente
        chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")
        if chromedriver_path and os.path.exists(chromedriver_path):
            if system != "windows":
                os.chmod(chromedriver_path, 0o755)
            return chromedriver_path
        
        # Última tentativa: procura no PATH do sistema
        import shutil
        chromedriver_in_path = shutil.which("chromedriver")
        if chromedriver_in_path:
            return chromedriver_in_path
        
        raise Exception(
            f"Não foi possível encontrar o ChromeDriver. "
            f"Erro do webdriver-manager: {str(e)}. "
            f"Coloque o chromedriver no diretório do projeto ou defina CHROMEDRIVER_PATH."
        )


@pytest.fixture(scope="function")
def driver():
    """
    Fixture que inicializa e finaliza o WebDriver para cada teste.
    Utiliza ChromeDriver local ou gerenciado automaticamente.
    """
    chrome_options = Options()
    # Descomente a linha abaixo para executar em modo headless (sem interface gráfica)
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    try:
        chromedriver_path = get_chromedriver_path()
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        pytest.fail(f"Falha ao inicializar o WebDriver: {str(e)}")
    
    yield driver
    
    driver.quit()


@pytest.fixture
def base_url():
    """URL base da aplicação."""
    return "http://localhost:3001"


@pytest.fixture
def valid_credentials():
    """Credenciais válidas para login."""
    return {
        "email": "test@universitypresence.com",
        "password": "123456"
    }

