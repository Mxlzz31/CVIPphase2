import tkinter as tk
import sounddevice as sd
import wavio
import os
from datetime import datetime

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder App")

        self.is_recording = False
        self.recording_filename = None

        # UI components
        self.record_button = tk.Button(root, text="Record", command=self.toggle_recording)
        self.record_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        # Start the GUI event loop
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        root.mainloop()

    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(text="Stop Recording")
        self.save_button.config(state=tk.DISABLED)

        # Set up audio recording
        self.recording_filename = f"/Users\logan\Desktop{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        self.stream = sd.InputStream(callback=self.audio_callback)
        self.stream.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(text="Record")
        self.save_button.config(state=tk.NORMAL)

        # Stop audio recording
        self.stream.stop()
        self.stream.close()

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        wavio.write(self.recording_filename, indata, 44100, sampwidth=3)

    def save_recording(self):
        save_path = tk.filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if save_path:
            os.rename(self.recording_filename, save_path)
            tk.messagebox.showinfo("Save Recording", "Recording saved successfully!")

    def on_closing(self):
        if self.is_recording:
            self.stop_recording()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
