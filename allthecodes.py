import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

def send_messages():
    try:
        text = entry_message.get()
        count = int(entry_count.get())
        cooldown = float(entry_cooldown.get())

        if not text or count <= 0:
            messagebox.showwarning("Spam Bot", "Enter valid values")
            return

        messagebox.showinfo("Spam Bot", "You have 5 seconds to open Whatsapp or another messenger app to spam your messages!")
        time.sleep(5)

        for _ in range(count):
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            time.sleep(cooldown)

        messagebox.showinfo("Spam Bot", "Task Completed! Please follow Deniz Software for support.")

    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu: {e}")

# Tkinter Arayüzü
root = tk.Tk()
root.title("WhatsApp Spam Bot (Beta)")
root.geometry("350x350")
root.resizable(False, False)

# Fontu Türkçe karakterler için uygun bir fontla değiştir

tk.Label(root, text="Enter Text:", relief="flat", font=("Arial", 20, "bold")).pack(pady=5)
entry_message = tk.Entry(root, width=40, relief="flat", font=("Arial", 20, "bold"))  # Fontu burada belirledik
entry_message.pack(pady=5)

tk.Label(root, text="Repeat Count", relief="flat", font=("Arial", 12, "bold")).pack(pady=5)
entry_count = tk.Entry(root, width=10, relief="flat", font=("Arial", 20, "bold"))
entry_count.pack(pady=5)

tk.Label(root, text="Cooldown(Second)", relief="flat", font=("Arial", 12, "bold")).pack(pady=5)
entry_cooldown = tk.Entry(root, width=10, relief="flat", font=("Arial", 20, "bold"))
entry_cooldown.pack(pady=5)
entry_cooldown.insert(0, "0.5")

btn_send = tk.Button(root, text="Send", command=send_messages, bg="green", fg="white", relief="flat", width=20, height=2)
btn_send.pack(pady=10)

root.mainloop()
