# ----------------------------------------------------------------
# Author: Michael Collins, Christopher Davis, Toria Evans
# Date: 11/16/21
#
# This module calculates billing information
# for students in the class registration system. Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    total_hours = 0
    credits_cost = 0
    for i in c_rosters:
        if id in c_rosters[i]:
            total_hours += c_hours[i]
    if s_in_state[id] is True:
        credits_cost = 225
    elif s_in_state[id] is False:
        credits_cost = 850
    total_cost = total_hours * credits_cost
    return total_hours, float(total_cost)
