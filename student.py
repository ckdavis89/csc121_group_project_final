# ----------------------------------------------------------------
# Author: Michael Collins, Christopher Davis, Toria Evans
# Date: 11/16/21
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------
import tkinter.messagebox


def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function counts courses a student has registered for
    # and creates a list that it returns to the main function.
    # It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters.
    # -------------------------------------------------------------
    course_list = []
    for i in c_roster:
        if id in c_roster[i]:
            course_list.append(i)
    joined_list = '\n'.join(course_list)
    return joined_list, course_list


def add_course(id, c_choice, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added;
    # c_choice is the course they want to add; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # If student has already registered for this course, it displays
    # an error message.
    # If the course is full, it displays an error message.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    response = c_choice
    if response not in c_roster.keys():
        tkinter.messagebox.showerror('Error', 'Please select a course')
    elif id in c_roster[response]:
        tkinter.messagebox.showerror('Error', 'You are already enrolled in that course.')
    elif len(c_roster[response]) == c_max_size[response]:
        tkinter.messagebox.showerror('Error', 'Course is already full')
    else:
        c_roster[response].append(id)
        tkinter.messagebox.showinfo('Success', 'Course registered')


def drop_course(id, c_choice, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_choice is the desired course to drop; c_roster is the list
    # of class rosters. If the course is not offered, it displays
    # an error message. If the student is not enrolled in that course,
    # it displays an error message.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem. This function has no return value.
    # -------------------------------------------------------------
    if c_choice not in c_roster.keys():
        tkinter.messagebox.showerror('Error', 'Please select a course')
    elif id not in c_roster[c_choice]:
        tkinter.messagebox.showerror('Error', 'You are not enrolled in that course')
    else:
        c_roster[c_choice].remove(id)
        tkinter.messagebox.showinfo('Success', 'Course Dropped')
