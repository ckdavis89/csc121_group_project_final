# ----------------------------------------------------------------
# Author: Michael Collins, Christopher Davis, Toria Evans
# Date: 11/16/21
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# costs for their course roster.
# -----------------------------------------------------------------
import billing
import student
import tkinter
import tkinter.ttk
import tkinter.messagebox

student_list = [('1001', '111'), ('1002', '222'),
                ('1003', '333'), ('1004', '444')]
student_in_state = {'1001': True,
                    '1002': False,
                    '1003': True,
                    '1004': False}
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'],
                 'CSC102': ['1001'],
                 'CSC103': ['1002'],
                 'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message.
    # -------------------------------------------------------------
    pin = pin_entry.get()
    if (id, pin) in s_list:
        tkinter.messagebox.showinfo('Success', 'ID and PIN verified.')
        main_window.withdraw()
        main()
    elif (id, pin) not in s_list:
        tkinter.messagebox.showerror('Error', 'The ID or PIN entered is incorrect.')


def main():
    # create the registration window
    register_window = tkinter.Toplevel(main_window)
    register_window.title('Registration')
    register_window.geometry("450x200")

    # Convert the window to a Notebook and add the tabs with their corresponding titles
    notebook = tkinter.ttk.Notebook(register_window)
    tab1 = tkinter.ttk.Frame(notebook)
    tab2 = tkinter.ttk.Frame(notebook)
    tab3 = tkinter.ttk.Frame(notebook)
    tab4 = tkinter.ttk.Frame(notebook)
    notebook.add(tab1, text='Add/Drop')
    notebook.add(tab2, text='List Courses')
    notebook.add(tab3, text='Billing')
    notebook.add(tab4, text='Sign Out')
    notebook.pack(expand=2, fill='both')

    # Put the labels and buttons on the add/drop page to let a student add or drop a course
    frame1 = tkinter.Frame(tab1)
    frame2 = tkinter.Frame(tab1)
    frame1.pack()
    frame2.pack()
    radio_choice = tkinter.StringVar()
    for course in course_roster:
        radio = tkinter.ttk.Radiobutton(frame1, text=course, value=course, variable=radio_choice)
        radio.pack()
    add_course = tkinter.Button(frame2, text='Add Course', command=lambda: [
        student.add_course(id_entry.get(), radio_choice.get(), course_roster, course_max_size)])
    add_course.pack(side='left')
    drop_course = tkinter.Button(frame2, text='Drop Course', command=lambda: [
        student.drop_course(id_entry.get(), radio_choice.get(), course_roster)])
    drop_course.pack(side='left')

    # Put labels and button on page to list a students registered courses
    list_course = tkinter.Frame(tab2)
    num_course = tkinter.Frame(tab2)
    course_button = tkinter.Frame(tab2)
    course_label = tkinter.Label(list_course, text='Registered Courses:')
    courses = tkinter.StringVar()
    courses_return = tkinter.Label(list_course, textvariable=courses)
    num_label = tkinter.Label(num_course, text='Total number:')
    num = tkinter.IntVar()
    num_return = tkinter.Label(num_course, textvariable=num)
    update_button = tkinter.Button(course_button, text='Update',
                                   command=lambda: [courses.set(student.list_courses(id_entry.get(), course_roster)[0]),
                                                    num.set(
                                                        len(student.list_courses(id_entry.get(), course_roster)[1]))])
    list_course.pack()
    num_course.pack()
    course_button.pack()
    course_label.pack()
    courses_return.pack()
    num_label.pack(side='left')
    num_return.pack(side='left')
    update_button.pack()

    # Place labels and buttons on the billing page to show student billing information
    bill1 = tkinter.Frame(tab3)
    bill2 = tkinter.Frame(tab3)
    bill3 = tkinter.Frame(tab3)
    hours_label = tkinter.Label(bill1, text='Total Credit Hours:')
    credit_hours = tkinter.StringVar()
    credit_hours_return = tkinter.Label(bill1, textvariable=credit_hours)
    credit_hours.set('0')
    total_label = tkinter.Label(bill2, text='Enrollment Cost: $')
    total = tkinter.StringVar()
    total_return = tkinter.Label(bill2, textvariable=total)
    total.set('0.00')
    calculate = tkinter.Button(bill3, text='Calculate', command=lambda: [credit_hours.set(
        billing.calculate_hours_and_bill(id_entry.get(), student_in_state, course_roster, course_hours)[0]), total.set(
        billing.calculate_hours_and_bill(id_entry.get(), student_in_state, course_roster, course_hours)[1])])
    hours_label.pack(side='left')
    credit_hours_return.pack(side='left')
    total_label.pack(side='left')
    total_return.pack(side='left')
    calculate.pack()
    bill1.pack()
    bill2.pack()
    bill3.pack()

    # Place a button that signs out of the application and returns to the login window
    sign_out = tkinter.Button(tab4, text='Sign Out',
                              command=lambda: [register_window.destroy(), main_window.deiconify()],
                              font=('Helvetica bold', 15))
    sign_out.pack()


# Create the login page and initialize .
main_window = tkinter.Tk()
main_window.title('Student Registration Login')
main_window.geometry("450x100")
top_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)
top_frame.pack()
bottom_frame.pack()
id_label = tkinter.Label(top_frame, text='ID:', font=('Helvetica bold', 15))
id_entry = tkinter.Entry(top_frame, width=10, font=('Helvetica bold', 15))
pin_label = tkinter.Label(top_frame, text='Pin:', font=('Helvetica bold', 15))
pin_entry = tkinter.Entry(top_frame, width=10, font=('Helvetica bold', 15))
log_in_button = tkinter.Button(bottom_frame, text='Log in', command=lambda: login(id_entry.get(), student_list),
                               font=('Helvetica bold', 15))
quit_button = tkinter.Button(bottom_frame, text='Quit', command=main_window.destroy, font=('Helvetica bold', 15))
id_label.pack(side='left')
id_entry.pack(side='left')
pin_label.pack(side='left')
pin_entry.pack(side='left')
log_in_button.pack(side='left')
quit_button.pack(side='left')
main_window.mainloop()
