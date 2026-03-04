from tkinter import *
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # pillow library for images.
from tkinter import messagebox
import mysql.connector
import cv2


# python "d:/sem 5/project/Face_recognization/student.py"


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # --------- variables -------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # first image
        img = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\student_att.png"
        )  # r is used for autmotically convert back slash to forward slash
        img = img.resize(
            (500, 130), Image.LANCZOS
        )  # antialias is used to convert image to high level to low level
        self.photoimg = ImageTk.PhotoImage(img)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\studface.png"
        )  # r is used for autmotically convert back slash to forward slash
        img1 = img1.resize(
            (500, 130), Image.LANCZOS
        )  # antialias is used to convert image to high level to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        # third Image
        img2 = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\student3.jpg"
        )  # r is used for autmotically convert back slash to forward slash
        img2 = img2.resize(
            (500, 130), Image.LANCZOS
        )  # antialias is used to convert image to high level to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # to save on window
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # background image
        img3 = Image.open(r"D:\sem 5\project\Face_recognization\clg_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # To place on window
        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_image,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Helvetica", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_image, bd=2, bg="white")
        main_frame.place(x=50, y=55, width=1500, height=600)

        # left label frame

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="STUDENT DETAILS",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=5, width=750, height=580)
        # left image

        img_left = Image.open(
            r"D:\sem 5\project\Face_recognization\clg_images\comp.jpg"
        )
        img_left = img_left.resize((700, 220), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        # antialias is used to convert image to high level to low level
        # to save on window

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=10, width=730, height=130)
        # current course info
        current_course_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="CURRENT COURSE INFORMATION",
            font=("times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=135, width=730, height=130)

        # department
        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
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
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(
            current_course_frame,
            text="Course",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        course_combo["values"] = (
            "Select Course",
            "FE",
            "SE",
            "TE",
            "BE",
        )
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # sem
        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
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
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # sticky for widegt

        # year
        year_label = Label(
            current_course_frame,
            text="Year",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
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
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Class Student info
        class_student_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="CLASS STUDENT INFORMATION",
            font=("times new roman", 12, "bold"),
        )
        class_student_frame.place(x=5, y=270, width=730, height=280)

        # Student ID
        student_ID_label = Label(
            class_student_frame,
            text="Student ID:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        student_ID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_id,
            width=20,
            font=("Helvetica", 12, "bold"),
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
            class_student_frame,
            textvariable=self.var_name,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(
            class_student_frame,
            text="Class Division:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # combo..
        div_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_div,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll Number
        roll_num_label = Label(
            class_student_frame,
            text="Roll Number:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        roll_num_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_num_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        roll_num_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(
            class_student_frame,
            text="Gender:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=20,
        )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Age
        age_label = Label(
            class_student_frame, text="DOB:", font=("Helvetica", 12, "bold"), bg="white"
        )
        age_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        age_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        age_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(
            class_student_frame,
            text="Email:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_label = Label(
            class_student_frame,
            text="Phone Number:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(
            class_student_frame,
            text="Address:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_address,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_name_label = Label(
            class_student_frame,
            text="Teacher Name:",
            font=("Helvetica", 12, "bold"),
            bg="white",
        )
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("Helvetica", 12, "bold"),
        )
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio buttons Student's Status
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take a Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radiobtn2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=725, height=35)

        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=17,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)
        # Update
        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=17,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=17,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            width=17,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=230, width=725, height=35)

        take_photo_btn = Button(
            btn_frame1,
            command=self.generate_dataset,
            text="Take Photo Sample",
            width=35,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            width=35,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1)

        # right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=770, y=10, width=720, height=580)
        # main_frame.place(x=10, y=55, width=1500, height=600)

        img_right = Image.open(
            "D:\sem 5\project\Face_recognization\clg_images\Student1.jpg"
        )
        img_right = img_right.resize((700, 220), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        # antialias is used to convert image to high level to low level
        # to save on window

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=10, width=710, height=130)

        # === Search System ==========
        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(
            Search_frame,
            text="Search By:",
            font=("Helvetica", 15, "bold"),
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        # combo
        search_combo = ttk.Combobox(
            Search_frame,
            font=("Helvetica", 12, "bold"),
            state="readonly",
            width=17,
        )
        search_combo["values"] = (
            "Select",
            "Roll_no",
            "Phone_no",
        )
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=12, font=("Helvetica", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn = Button(
            Search_frame,
            text="Search",
            width=10,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Search_btn.grid(row=0, column=3, padx=4)

        Show_All_btn = Button(
            Search_frame,
            text="Show All",
            width=10,
            font=("Helvetica", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Show_All_btn.grid(row=0, column=4, padx=4)

        # =============Table Frame ===================
        Table_frame = Frame(
            Right_frame,
            bd=2,
            relief=RIDGE,
        )
        Table_frame.place(x=5, y=210, width=710, height=350)

        scrool_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scrool_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            Table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scrool_x.set,
            yscrollcommand=scrool_y.set,
        )

        scrool_x.pack(side=BOTTOM, fill=X)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_x.config(command=self.student_table.xview)
        scrool_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        # set width
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)  # packed the table
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # Place the main frame
        main_frame.place(x=10, y=55, width=1500, height=600)

    # === ========== Function Declaration=================
    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
            or self.var_roll.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Change "username" to "user"
                    password="vruddhishahmomdad17",
                    database="face_recognization",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student Details Has been Added Successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #  --------------------- Fetching the data -----------
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change "username" to "user"
            password="vruddhishahmomdad17",
            database="face_recognization",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # -------------- Get Cursor ----------------------
    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if len(data) >= 15:
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_id.set(data[4]),
            self.var_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14]),
        else:
            messagebox.showerror(
                "Error", "Data is incomplete or missing", parent=self.root
            )

    # ----------- Update Function -------------------
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
            or self.var_roll.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do You want to update the student Details ?",
                    parent=self.root,
                )
                # Update=messagebox.askyesno("Update","Do You want to update the student Details ?",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",  # Change "username" to "user"
                        password="vruddhishahmomdad17",
                        database="face_recognization",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Divison=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_id.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Updated Successfully!", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ------------- Delete Function -----------------
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student ?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",  # Change "username" to "user"
                        password="vruddhishahmomdad17",
                        database="face_recognization",
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo(
                        "Delete",
                        "Succesfully Deleted Student Details!!",
                        parent=self.root,
                    )

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ----------  Genrate data set  or Take photo sample -----------

    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
            or self.var_roll.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Change "username" to "user"
                    password="vruddhishahmomdad17",
                    database="face_recognization",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute(
                    "UPDATE student SET dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Divison=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ------ Load Predefined data on face frontals from Open Cv -------

                face_classifier = cv2.CascadeClassifier(
                    "D:\sem 5\project\Face_recognization\haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # scaling factor->1.3
                    # minimum neighbor->5

                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        if not face_cropped.size == 0:
                            return face_cropped
                    return None

                cap = cv2.VideoCapture(0)

                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    cv2.imshow("Camera", my_frame)

                    #if ret:  # Check if the frame was captured successfully
                    face = face_cropped(my_frame)

                    if face is not None and face.size !=0:
                                                                img_id += 1
                    
                    '''desired_size = (450, 450)
                    face = cv2.resize(face, desired_size, interpolation=cv2.INTER_AREA)'''

                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(
                        face,
                        str(img_id),
                        (50, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        2,
                        (0, 255, 0),
                        2,
                    )
                    cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or cv2.waitKey(1) == ord("q"):
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.geometry("1530x790+0+0")
    root.title("Face Recognition System")
    root.mainloop()
