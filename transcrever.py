import whisper

def transcribe_audio(audio_path):
  """
    Transcreve o áudio com timestamps e parágrafos com base nas pausas.
  """
  print("🔊 Iniciando transcrição...")
  model = whisper.load_model("large") # ou "base", "medium"
  result = model.transcribe(audio_path)
  print("✅ Transcrição concluída!\n")
  return result['segments']

def format_segments(segments):
  """
    Formata os segmentos com timestamps e quebra de linha por frase.
  """
  transcript = ""
  for seg in segments:
    start = seg['start']
    end = seg['end']
    text = seg['text'].strip()

    # Formata timestamp no estilo [00:00:03 - 00:00:08]
    timestamp = f"[{format_time(start)} - {format_time(end)}]"
    transcript += f"{timestamp} {text}\n\n"
  return transcript

def format_time(seconds):
  """
    Converte segundos em formato hh:mm:ss.
  """
  h = int(seconds // 3600)
  m = int((seconds % 3600) // 60)
  s = int(seconds % 60)
  return f"{h:02}:{m:02}:{s:02}"

def main():
  audio_file = "audio.m4a" # Escreva o nome do arquivo e a extensão desejada
  output_file = "transcricao.txt"

  segments = transcribe_audio(audio_file)
  formatted_text = format_segments(segments)

  with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_text)

  print(f"💾 Transcrição salva em: {output_file}")

if __name__ == "__main__":
  main()
