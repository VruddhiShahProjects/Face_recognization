from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Images
        img = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\student_att.png"
        )
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        img1 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\studface.png"
        )
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\student3.jpg"
        )
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Title
        title_lbl = Label(
            root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Helvetica", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        bg_image = Label(root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        # Left Frame
        Left_frame = LabelFrame(
            bg_image,
            bd=2,
            relief=RIDGE,
            text="STUDENT DETAILS",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=55, width=800, height=500)

        # Left Images
        f_lbl = Label(Left_frame, image=self.photoimg)
        f_lbl.place(x=5, y=0, width=780, height=130)

        # Current Course Info
        current_course_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="CURRENT COURSE IMPORTANCE",
            font=("times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=135, width=780, height=130)

        # Department
        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(
            current_course_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer",
            "IT",
            "Civil",
            "Mechanical",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Course
        course_label = Label(
            current_course_frame,
            text="Course",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(
            current_course_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Semester
        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(
            current_course_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        semester_combo["values"] = (
            "Select Semester",
            "Semester-1",
            "Semester-2",
            "Semester-3",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Year
        year_label = Label(
            current_course_frame,
            text="Year",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(
            current_course_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        year_combo["values"] = (
            "Select Year",
            "2020-2021",
            "2021-2022",
            "2022-2023",
            "2023-2024",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Class Student Info
        class_student_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="CLASS STUDENT INFORMATION",
            font=("times new roman", 12, "bold"),
        )
        class_student_frame.place(x=5, y=270, width=780, height=200)

        # Student ID
        student_ID_label = Label(
            class_student_frame,
            text="Student ID:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        student_ID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        student_Name_label = Label(
            class_student_frame,
            text="Student Name:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        student_Name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(
            class_student_frame,
            text="Class Division:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5)

        # Class Division Entry
        class_div_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        class_div_entry.grid(row=1, column=1, padx=10, pady=5)

        # Roll Number
        roll_num_label = Label(
            class_student_frame,
            text="Roll Number:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        roll_num_label.grid(row=1, column=2, padx=10, pady=5)

        roll_num_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        roll_num_entry.grid(row=1, column=3, padx=10, pady=5)

        # Gender
        gender_label = Label(
            class_student_frame,
            text="Gender:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5)

        gender_combo = ttk.Combobox(
            class_student_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5)

        # Age
        age_label = Label(
            class_student_frame, text="Age:", font=("Helvetica", 12, "bold"), bg="white"
        )
        age_label.grid(row=2, column=2, padx=10, pady=5)

        age_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        age_entry.grid(row=2, column=3, padx=10, pady=5)

        # Email
        email_label = Label(
            class_student_frame,
            text="Email:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        email_label.grid(row=3, column=0, padx=10, pady=5)

        email_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        email_entry.grid(row=3, column=1, padx=10, pady=5)

        # Phone Number
        phone_label = Label(
            class_student_frame,
            text="Phone Number:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5)

        phone_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5)

        # Address
        address_label = Label(
            class_student_frame,
            text="Address:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        address_label.grid(row=4, column=0, padx=10, pady=5)

        address_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        address_entry.grid(row=4, column=1, padx=10, pady=5)

        # Teacher Name
        teacher_name_label = Label(
            class_student_frame,
            text="Teacher Name:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5)

        teacher_name_entry = ttk.Entry(
            class_student_frame, width=20, font=("Helvetica", 12, "bold")
        )
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5)

        # Radio Buttons for Student's Status
       # self.var_radio1 = StringVar()
        #self.var_radio1.set("Active")

        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            text="Take Photo Sample",
            #variable=self.var_radio1,
            value="Active",
            #font=("Helvetica", 11, "bold"),
            #bg="white",
        )
        radiobtn1.grid(row=5, column=0, padx=2, pady=5)

        '''radio_inactive = Radiobutton(
            class_student_frame,
            text="Inactive",
            variable=self.var_radio1,
            value="Inactive",
            font=("Helvetica", 11, "bold"),
            bg="white",
        )
        radio_inactive.grid(row=5, column=1, padx=2, pady=5)
'''
        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=775, height=35)

        # Buttons
        add_btn = Button(btn_frame, text="Add", width=15, command=self.add_students)
        add_btn.grid(row=0, column=0, padx=5)

        update_btn = Button(
            btn_frame, text="Update", width=15, command=self.update_data
        )
        update_btn.grid(row=0, column=1, padx=5)

        delete_btn = Button(
            btn_frame, text="Delete", width=15, command=self.delete_data
        )
        delete_btn.grid(row=0, column=2, padx=5)

        reset_btn = Button(btn_frame, text="Reset", width=15, command=self.reset_data)
        reset_btn.grid(row=0, column=3, padx=5)

        take_photo_btn = Button(
            btn_frame, text="Take Photo", width=15, command=self.take_photo
        )
        take_photo_btn.grid(row=0, column=4, padx=5)

        # Right Frame
        Right_frame = LabelFrame(
            bg_image,
            bd=2,
            relief=RIDGE,
            text="STUDENT DETAILS",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=830, y=55, width=700, height=500)

        # Image Banner
        img2_lbl = Label(Right_frame, image=self.photoimg1)
        img2_lbl.place(x=5, y=0, width=680, height=130)

        # Search System
        search_frame = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        search_frame.place(x=5, y=135, width=680, height=70)

        search_combo = ttk.Combobox(
            search_frame, font=("Helvetica", 12, "bold"), state="readonly", width=20
        )
        search_combo["values"] = ("Select", "Roll No.", "Phone No.", "Name")
        search_combo.grid(row=0, column=0, padx=10, pady=5)

        search_entry = ttk.Entry(search_frame, font=("Helvetica", 12, "bold"), width=20)
        search_entry.grid(row=0, column=1, padx=2, pady=5)

        search_btn = Button(search_frame, text="Search", width=15)
        search_btn.grid(row=0, column=2, padx=5)

        show_all_btn = Button(search_frame, text="Show All", width=15)
        show_all_btn.grid(row=0, column=3, padx=5)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=680, height=280)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "sem",
                "year",
                "ID",
                "name",
                "div",
                "roll",
                "gender",
                "age",
                "email",
                "phone",
                "address",
                "teacher",
                "status",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("status", text="Status")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("age", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("status", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

    def add_students(self):
        # Code to add student information to the database
        pass

    def update_data(self):
        # Code to update student information in the database
        pass

    def delete_data(self):
        # Code to delete student information from the database
        pass

    def reset_data(self):
        # Code to reset the input fields
        pass

    def take_photo(self):
        # Code to capture student's photo using a camera or webcam
        pass


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
