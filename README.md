# 🚀 Web Scraping com Selenium - Extração de Links

## 📌 Descrição do Projeto
Este projeto utiliza **Selenium** para extrair links de páginas da web automaticamente. O script acessa sites específicos, coleta URLs de todos os links presentes e armazena essas informações em arquivos de texto para posterior análise.

## 🛠️ Tecnologias Utilizadas
- **Python** 🐍
- **Selenium** 🌐
- **Google Chrome & ChromeDriver** 🖥️

## 📂 Estrutura do Projeto
```
📁 projeto-web-scraping
│-- 📄 main.py            # Código principal do script
│-- 📄 Arch.txt           # Arquivo com a lista numerada de links extraídos
│-- 📄 Hrefs.txt          # Arquivo com os links extraídos
│-- 📄 Extracion.txt      # Arquivo com os links processados
│-- 📂 chromedriver-win64 # Pasta com o ChromeDriver
│   ├── chromedriver.exe
```

## 📦 Instalação e Configuração
### 1️⃣ Instalar dependências
Antes de rodar o script, instale as bibliotecas necessárias:
```sh
pip install selenium
```

### 2️⃣ Baixar o ChromeDriver
O **ChromeDriver** deve ser compatível com a versão do seu Google Chrome. Faça o download em:
[ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

Coloque o executável na pasta `chromedriver-win64` e ajuste o caminho no código, se necessário:
```python
service = Service('./chromedriver-win64/chromedriver.exe')
```

## 🚀 Como Executar o Script
1. Abra o terminal e navegue até a pasta do projeto:
   ```sh
   cd caminho/para/o/projeto
   ```
2. Execute o script principal:
   ```sh
   python main.py
   ```

## 🔍 Como Funciona o Código
### 🔹 Etapa 1: Extração de Links
- O script acessa a **Wikipedia** e coleta todos os links (`<a>` tags) da página.
- Os links são salvos nos arquivos `Arch.txt` e `Hrefs.txt`.

### 🔹 Etapa 2: Acesso e Processamento dos Links
- Lê os links do `Hrefs.txt` e acessa cada um deles.
- Filtra e salva os URLs finais no arquivo `Extracion.txt`.

## ⚠️ Possíveis Problemas e Soluções
| Erro | Solução |
|------|---------|
| `selenium.common.exceptions.WebDriverException` | Verifique se o ChromeDriver está no caminho correto. |
| `TimeoutException` | Tente aumentar o tempo de espera no `WebDriverWait`. |
| `PermissionError` | Execute o terminal com permissões de administrador. |

## 📝 Melhorias Futuras
- Melhor tratamento de erros e exceções.
- Implementação de multithreading para maior velocidade.
- Adicionar suporte para diferentes navegadores.

---
Feito com ❤️ por [Seu Nome] 🚀

