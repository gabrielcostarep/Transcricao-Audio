import whisper
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading

def format_time(seconds):
  hours = int(seconds // 3600)
  minutes = int((seconds % 3600) // 60)
  secs = int(seconds % 60)
  return f"{hours:02}:{minutes:02}:{secs:02}"

def format_segments(segments):
  transcript = ""
  for segment in segments:
    start = segment['start']
    end = segment['end']
    text = segment['text'].strip()
    timestamp = f"[{format_time(start)} - {format_time(end)}]"
    transcript += f"{timestamp} {text}\n\n"
  return transcript

def safe_update_status(message):
  def update():
    if root.winfo_exists():
      status_label.config(text=message)
  root.after(0, update)

def safe_set_button_state(state):
  def update():
    if root.winfo_exists():
      select_button.config(state=state)
  root.after(0, update)

def transcribe_audio(audio_path, output_dir):
  try:
    safe_update_status("🔊 Carregando modelo...")
    model = whisper.load_model("large")
    
    safe_update_status("⏳ Transcrevendo...")
    result = model.transcribe(audio_path)
    
    transcript = format_segments(result['segments'])

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_transcricao.txt")

    with open(output_path, "w", encoding="utf-8") as file:
      file.write(transcript)

    messagebox.showinfo("Sucesso", f"💾 Transcrição salva em:\n{output_path}")

  except Exception as error:
    messagebox.showerror("Erro", f"🚨 Ocorreu um erro durante a transcrição:\n{str(error)}")

  finally:
    safe_set_button_state("normal")
    safe_update_status("Pronto para uma nova transcrição.")

def transcribe_audio_thread(audio_path, output_dir):
  transcribe_audio(audio_path, output_dir)

def select_audio_file():
  audio_path = filedialog.askopenfilename(
    initialdir=os.path.dirname(os.path.abspath(__file__)),
    title="Selecione um arquivo de áudio",
    filetypes=[
      ("Áudios suportados", "*.mp3 *.m4a *.wav *.ogg *.flac *.webm *.mp4"),
      ("Todos os arquivos", "*.*")
    ]
  )
  if audio_path:
    output_dir = filedialog.askdirectory(
      initialdir=os.path.dirname(os.path.abspath(__file__)),
      title="Selecione a pasta de saída"
    )
    if not output_dir:
      output_dir = os.getcwd()

    select_button.config(state="disabled")
    safe_update_status("Iniciando transcrição...")

    threading.Thread(target=transcribe_audio_thread, args=(audio_path, output_dir), daemon=True).start()

def cancel_program():
  root.destroy()

root = tk.Tk()
root.title("Transcritor Whisper")
root.geometry("400x180")

label = tk.Label(root, text="Selecione um arquivo de áudio para transcrever", pady=20)
label.pack()

select_button = tk.Button(root, text="Escolher arquivo", command=select_audio_file)
select_button.pack(pady=(0,10))

status_label = tk.Label(root, text="Aguardando seleção...", pady=10)
status_label.pack()

cancel_button = tk.Button(root, text="Cancelar", fg="black", command=cancel_program)
cancel_button.pack()

root.mainloop()
