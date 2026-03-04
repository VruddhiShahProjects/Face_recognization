from tkinter import *
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # pillow library for images.
from student import Student


class Face_Recognization_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\mainpagelj.jpg"
        )  # r is used for autmotically convert back slash to forward slash
        img = img.resize(
            (500, 130), Image.ANTIALIAS
        )  # antialias is used to convert image to high level to low level
        self.photoimg = ImageTk.PhotoImage(img)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\2nd.png"
        )  # r is used for autmotically convert back slash to forward slash
        img1 = img1.resize(
            (500, 130), Image.ANTIALIAS
        )  # antialias is used to convert image to high level to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        # third Image
        img2 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\third.jpg"
        )  # r is used for autmotically convert back slash to forward slash
        img2 = img2.resize(
            (500, 130), Image.ANTIALIAS
        )  # antialias is used to convert image to high level to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # background image
        img3 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # To place on window
        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_image,
            text="FACE RECOGNIZATION ATTENDANCE SYSTEM SOFTWARE",
            font=("Helvetica", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # student button
        img4 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\student.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_image, command=self.student_details, image=self.photoimg4, cursor="hand2"
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_image,
            command=self.student_details,
            text="Student Details",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detact Face button
        img5 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\face.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="Face Detector",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance FAce button
        img6 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\attendance.png"
        )
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_image, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="Attendance ",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=300, width=220, height=40)

        # HElp
        img7 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_image, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="HELP DESK",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Face button
        img8 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_image, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="TRAIN DATA",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos
        img9 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\image.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_image, image=self.photoimg9, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="PHOTOS",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=500, y=580, width=220, height=40)

        # Devloper
        img10 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\devloper.jpg"
        )
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_image, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="DEVLOPER",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit
        img11 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_image, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(
            bg_image,
            text="EXIT",
            cursor="hand2",
            font=("Helvetica", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=1100, y=580, width=220, height=40)

    # ============== Function Buttons ===================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization_System(root)
    root.mainloop()
