

"""
The Problem: "The Appointment Finder"
Prompt: You are given a list of a therapist's busy_slots (already booked appointments) and a work_day range. You need to find all available time slots of a specific duration (e.g., 30 minutes) where a patient can book an appointment.

Example Scenario:
Work Day: 09:00 to 12:00 (represented as minutes from midnight: 540 to 720)

Busy Slots: [[600, 630], [645, 700]]

Duration: 30 minutes

Output: [[540, 570], [570, 600]] (The gap between 630 and 645 is only 15 mins, so it's too short).
"""
from typing import List



def find_available_spots(busy_slots: List[List], workday_start: int, workday_end: int, duration: int):
    available = []
    current_time = workday_start
    busy_slots.sort(key=lambda x: x[0])

    for start, end in busy_slots:
        while current_time+duration <= start:
            available.append([current_time, current_time+duration])
            current_time += duration

        current_time = max(current_time, end)

    while current_time+duration <= workday_end:
        available.append([current_time, current_time+duration])
        current_time += duration

    return available


print(f"output: {find_available_spots([[600, 630], [645, 700]], 540, 720, 30)}")
assert find_available_spots([[540, 570], [570, 600]], 540, 720, 30) == [[540, 570], [570, 600]]
