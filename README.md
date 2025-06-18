# 🧠 Transcrição de Áudio com Whisper

Este projeto utiliza o modelo [Whisper](https://github.com/openai/whisper) da OpenAI para realizar transcrição automática de arquivos de áudio. Ele identifica pausas e gera parágrafos com **timestamps** no formato `[hh:mm:ss - hh:mm:ss]`.

---

## 🚀 Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/gabrielcostarep/Transcricao-Audio.git
cd transcricao-audio
```

### 2. Crie um ambiente virtual

```diff
python -m venv venv
```

Linux/macOS
```diff
source ./venv/bin/activate
```

Windows
```diff
venv\Scripts\activate 
```

### 3. Instale as dependências

```diff
pip install -r requirements.txt
```

## ▶️ Como Usar

1. Coloque seu arquivo de áudio (por exemplo, audio.m4a) na raiz do projeto.

2. Edite o nome do arquivo dentro da função main() se necessário.

3. Execute o script:

```diff
python transcrever.py
```

## 📄 Saída

O script gera um arquivo transcricao.txt com a transcrição formatada.

Cada bloco tem timestamp com início e fim, exemplo:
```
[00:00:03 - 00:00:08] Olá, tudo bem com você?

[00:00:09 - 00:00:12] Este é um exemplo de transcrição com tempo.
```