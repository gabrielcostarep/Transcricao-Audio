
# 🧠 Transcrição de Áudio com Whisper (Interface Gráfica)

Este projeto utiliza o modelo [Whisper](https://github.com/openai/whisper) da OpenAI para realizar transcrição automática de arquivos de áudio. Ele identifica pausas e gera parágrafos com **timestamps** no formato `[hh:mm:ss - hh:mm:ss]`.

> ⚠️ **Importante:** O Whisper deve ser executado com **Python 3.11** para garantir compatibilidade e funcionamento correto.

---

## 🚀 Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/gabrielcostarep/Transcricao-Audio.git
cd transcricao-audio
```

### 2. Crie e ative um ambiente virtual com Python 3.11

> Certifique-se de que o Python 3.11 está instalado no seu sistema. Você pode gerenciar versões com [pyenv](https://github.com/pyenv/pyenv) ou instalar diretamente do site oficial.

```bash
python3.11 -m venv venv
```

No Linux/macOS:

```bash
source ./venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Usar

1. Execute o script principal da interface gráfica:

```bash
python3.11 transcrever.py
```

2. Na janela que abrir:

- Clique em **Escolher arquivo** para selecionar o áudio a ser transcrito (o diálogo abrirá no diretório do script).
- Escolha a pasta onde deseja salvar a transcrição (padrão é o diretório atual).
- Durante a transcrição, o botão **Escolher arquivo** ficará desabilitado para evitar novas seleções.
- Você pode clicar em **Cancelar** a qualquer momento para fechar o programa.
- O status da transcrição será mostrado na janela com mensagens e indicadores durante o processo.

---

## 📄 Saída

O arquivo de transcrição será salvo na pasta escolhida, com o mesmo nome do arquivo de áudio acrescido de `_transcricao.txt`.

Cada trecho da transcrição tem timestamp com início e fim, por exemplo:

```
[00:00:03 - 00:00:08] Olá, tudo bem com você?

[00:00:09 - 00:00:12] Este é um exemplo de transcrição com tempo.
```

---
