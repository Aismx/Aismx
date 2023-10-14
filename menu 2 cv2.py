import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Imagen a PDF")

        self.label = tk.Label(root, text="Convertir Imagen a PDF", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(root, width=500, height=300)
        self.canvas.pack()

        self.select_button = tk.Button(root, text="Seleccionar imagen", command=self.select_image, font=("Helvetica", 12))
        self.select_button.pack(pady=10)

        self.crop_button = tk.Button(root, text="Recortar imagen", command=self.toggle_crop, font=("Helvetica", 12))
        self.crop_button.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convertir a PDF", command=self.convert_to_pdf, state=tk.DISABLED, font=("Helvetica", 12))
        self.convert_button.pack(pady=5)

        self.close_button = tk.Button(root, text="Cerrar", command=self.close_window, font=("Helvetica", 12))
        self.close_button.pack(pady=10)

        self.image_path = None
        self.image_label = None
        self.cropping = False
        self.cropped_image = None

        self.root.bind("<Control-s>", self.save_cropped_image)

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Imagenes", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            self.image_path = file_path
            self.cropped_image = None
            self.cropping = False
            self.crop_button.config(state=tk.NORMAL)
            self.convert_button.config(state=tk.NORMAL)
            self.show_selected_image()

    def show_selected_image(self):
        if self.image_label:
            self.canvas.delete(self.image_label)

        image = Image.open(self.image_path)
        image.thumbnail((500, 300))
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label = self.canvas.create_image(
            250, 150, image=self.tk_image)

    def toggle_crop(self):
        if self.cropping:
            self.cropping = False
            self.crop_button.config(text="Recortar imagen")
            self.show_selected_image()
        else:
            self.cropping = True
            self.crop_button.config(text="desacer recorte")
            self.show_cropped_image()

    def show_cropped_image(self):
        if self.image_path and self.cropping:
            img = cv2.imread(self.image_path)
            if img is not None:
                x, y, w, h = cv2.selectROI("Recortar Imagen", img, False)
                if w > 0 and h > 0:
                    self.cropped_image = img[y:y+h, x:x+w]
                    self.show_cropped_tk_image()

    def show_cropped_tk_image(self):
        if self.cropped_image is not None:
            image = Image.fromarray(cv2.cvtColor(
                self.cropped_image, cv2.COLOR_BGR2RGB))
            image.thumbnail((500, 300))
            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label = self.canvas.create_image(
                250, 150, image=self.tk_image)

    def save_cropped_image(self, event=None):
        if self.cropped_image is not None:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".jpg", filetypes=[("Imagen JPEG", "*.jpg")])
            if save_path:
                cv2.imwrite(save_path, self.cropped_image)
                messagebox.showinfo(
                    "Guardado", "Recorte guardado exitosamente.")

    def convert_to_pdf(self):
        if self.cropped_image is not None:
            pdf_path = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
            if pdf_path:
                c = canvas.Canvas(pdf_path, pagesize=letter)
                image = Image.fromarray(cv2.cvtColor(
                    self.cropped_image, cv2.COLOR_BGR2RGB))
                width, height = image.size
                c.drawImage(image, 0, 0, width=width, height=height)
                c.save()

                messagebox.showinfo(
                    "Convertido a PDF", f"Imagen convertida a PDF y guardada como '{pdf_path}'")

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPdfConverter(root)
    root.mainloop()
