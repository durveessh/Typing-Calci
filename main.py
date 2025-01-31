import tkinter as tk
import random
import math

# Updated List of predefined paragraphs
paragraphs = [
    "The quick brown fox jumps over the lazy dog. This sentence includes all the alphabet letters, making it an excellent typing practice tool. It is often used to test typing devices and assess typing speed. Repeatedly typing this sentence enhances muscle memory, hand coordination, and overall typing accuracy over time.",
    "Typing speed is an essential skill in the digital age. Being able to type swiftly and accurately boosts productivity and communication in personal and professional domains. Consistent practice and perseverance are the keys to mastering this skill. By engaging in typing exercises, one can significantly improve words per minute and achieve daily task efficiency.",
    "Python is a versatile programming language widely used in various fields, from web development to machine learning. Its simplicity and vast library support make it an ideal choice for beginners and professionals. Learning Python opens doors to careers in data science, artificial intelligence, and software development.",
    "Good communication skills play a crucial role in personal and professional growth. Expressing ideas clearly and listening actively fosters trust and collaboration. Effective communication helps resolve conflicts, build relationships, and achieve goals, making it a vital skill for success in all areas of life.",
    "Consistency is the key to mastering any skill. Whether learning a language, improving typing speed, or developing a new hobby, regular practice and dedication yield remarkable results. Over time, this effort builds confidence, expertise, and a strong foundation for success.",
    "Reading is one of the most effective ways to expand your knowledge and improve critical thinking. Books, articles, and even blogs offer valuable insights into various topics. By dedicating time to reading every day, you can enhance your vocabulary, focus, and overall intellectual growth.",
    "Teamwork is essential for achieving common goals. By working together, individuals can combine their unique skills and perspectives to create innovative solutions. Collaboration fosters mutual respect, effective communication, and a shared sense of accomplishment, driving success in any group endeavor.",
    "The journey of a thousand miles begins with a single step. This quote reminds us to take initiative and start pursuing our goals, no matter how challenging they seem. Breaking tasks into smaller steps makes them more manageable and helps maintain consistent progress toward success."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("900x650")
        self.root.configure(bg="#e4e9f7")
        
        self.time_left = 60
        self.total_words = 0
        self.correct_words = 0
        self.selected_paragraph = random.choice(paragraphs)
        
        self.setup_ui()
    
    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg="#4A90E2", height=100)
        header_frame.pack(fill="x")
        
        heading = tk.Label(header_frame, text="Typing Speed Calculator", font=("Arial", 28, "bold"), bg="#4A90E2", fg="#ffffff")
        heading.pack(pady=20)
        
        content_frame = tk.Frame(self.root, bg="#e4e9f7")
        content_frame.pack(pady=20, padx=20)
        
        self.paragraph_label = tk.Label(content_frame, text=self.selected_paragraph, wraplength=800, font=("Arial", 14), justify="left", bg="#ffffff", fg="#333333", padx=10, pady=10, bd=2, relief="groove")
        self.paragraph_label.pack(pady=10)
        
        self.text_area = tk.Text(content_frame, height=6, width=80, font=("Arial", 14), state="disabled", bg="#ffffff", fg="#333333", bd=2, relief="groove", padx=10, pady=5)
        self.text_area.pack(pady=10)
        
        button_frame = tk.Frame(self.root, bg="#e4e9f7")
        button_frame.pack(pady=10)
        
        start_button = tk.Button(button_frame, text="Start Test", command=self.start_test, font=("Arial", 14), bg="#66bb6a", fg="white", activebackground="#43a047", padx=20, pady=5, relief="flat")
        start_button.grid(row=0, column=0, padx=20)
        
        reset_button = tk.Button(button_frame, text="Reset Test", command=self.reset_test, font=("Arial", 14), bg="#ef5350", fg="white", activebackground="#e53935", padx=20, pady=5, relief="flat")
        reset_button.grid(row=0, column=1, padx=20)
        
        self.timer_label = tk.Label(self.root, text="Time Left: 60s", font=("Arial", 18), bg="#e4e9f7", fg="#333333")
        self.timer_label.pack(pady=10)
    
    def start_test(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.focus()
        self.time_left = 60
        self.timer_label.config(text="Time Left: 60s")
        self.root.after(1000, self.update_timer)
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_test()
    
    def end_test(self):
        self.text_area.config(state="disabled")
        typed_text = self.text_area.get("1.0", tk.END).strip()
        typed_words = typed_text.split()
        original_words = self.selected_paragraph.split()
        
        self.total_words = len(typed_words)
        self.correct_words = sum(1 for i, word in enumerate(typed_words) if i < len(original_words) and word == original_words[i])
        
        wpm = self.correct_words
        accuracy = (self.correct_words / self.total_words) * 100 if self.total_words else 0
        self.show_results(wpm, accuracy)
    
    def show_results(self, wpm, accuracy):
        result_window = tk.Toplevel(self.root)
        result_window.title("Test Results")
        result_window.geometry("500x500")
        result_window.configure(bg="#e4e9f7")
        
        canvas = tk.Canvas(result_window, width=400, height=400, bg="#e4e9f7", highlightthickness=0)
        canvas.pack(pady=20)
        
        # Draw speedometer for WPM
        self.draw_speedometer(canvas, 200, 200, 150, wpm, "Words Per Minute (WPM)")
        
        # Display additional results
        info_label = tk.Label(result_window, text=f"Accuracy: {accuracy:.2f}%\nTotal Words Typed: {self.total_words}\nCorrect Words: {self.correct_words}", font=("Arial", 16), bg="#e4e9f7", fg="#333333")
        info_label.pack(pady=10)
    
    def draw_speedometer(self, canvas, x, y, radius, value, label):
        # Draw outer circle
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#ffffff", outline="#cccccc", width=2)
        
        # Draw numeric markings
        for i in range(0, 101, 10):
            angle = (i / 100) * 180 - 90
            inner_x = x + (radius - 20) * math.cos(math.radians(angle))
            inner_y = y + (radius - 20) * math.sin(math.radians(angle))
            outer_x = x + radius * math.cos(math.radians(angle))
            outer_y = y + radius * math.sin(math.radians(angle))
            canvas.create_line(inner_x, inner_y, outer_x, outer_y, fill="#333333", width=2)
            if i % 20 == 0:
                text_x = x + (radius - 40) * math.cos(math.radians(angle))
                text_y = y + (radius - 40) * math.sin(math.radians(angle))
                canvas.create_text(text_x, text_y, text=f"{i}", font=("Arial", 10), fill="#333333")
        
        # Draw pointer
        angle = (value / 100) * 180 - 90
        end_x = x + radius * 0.8 * math.cos(math.radians(angle))
        end_y = y + radius * 0.8 * math.sin(math.radians(angle))
        canvas.create_line(x, y, end_x, end_y, fill="#ff5722", width=4)
        
        # Add label
        canvas.create_text(x, y + radius + 30, text=f"{label}: {value}", font=("Arial", 14), fill="#333333")
    
    def reset_test(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.config(state="disabled")
        self.selected_paragraph = random.choice(paragraphs)
        self.paragraph_label.config(text=self.selected_paragraph)
        self.time_left = 60
        self.timer_label.config(text="Time Left: 60s")
        self.total_words = 0
        self.correct_words = 0

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
