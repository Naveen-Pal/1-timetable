import random
from PIL import Image, ImageDraw, ImageFont

def get_section(roll_number):
    rn = roll_number - 25110000
    if rn <= 73:  # Adjust these ranges based on actual section divisions
        return 1
    elif rn <= 145:
        return 2
    elif rn <= 215:
        return 3
    elif rn <= 288:
        return 4
    else:
        return 5

def generate_timetable(roll_number, inside_font_size=12, inside_box_size=(200, 70)):
    def random_color():
        return (random.randint(200, 255), random.randint(100, 255), random.randint(100, 255))
    
    roll_number = int(roll_number)
    if not 25110001 <= roll_number <= 25110361:
        print("Wrong Roll Number")
        exit(1)

    # Increased size of the timetable image
    timetable_image = Image.new('RGB', (2000, 1180), color='white')
    draw = ImageDraw.Draw(timetable_image)

    # Use a larger font for time slots and days
    font_size_large = 30
    font_large = ImageFont.load_default().font_variant(size=font_size_large)

    # Use default font for regular text
    font = ImageFont.load_default()

    # Use variable font size for inside text
    inside_font = ImageFont.load_default().font_variant(size=inside_font_size)

    # Define time slots and days
    time_slots = ["8:30 - 9:50", "10:00 - 11:20", "11:30 - 12:50", "13:00 - 14:00", "14:00 - 15:20", "15:30 - 16:50", "17:00 - 18:20"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # Get student's section
    section = get_section(roll_number)

    # Draw headers with white background
    for i, day in enumerate(days):
        draw.rectangle([(i * inside_box_size[0] + 200, 0), ((i + 1) * inside_box_size[0] + 200, 80)], fill="white", outline="black")
        draw.text((i * inside_box_size[0] + 240, 20), day, fill="black", font=font_large)

    # Draw time slots
    for i, time_slot in enumerate(time_slots):
        draw.rectangle([(0, i * 150 + 80), (200, (i + 1) * 150 + 80)], fill="white", outline="black")
        draw.text((20, i * 150 + 110), time_slot, fill="black", font=font_large)

        # Add course information for each slot
        for j, day in enumerate(days):
            box_size = inside_box_size
            
            # Draw box with random color
            if i != 3:  # Not lunch break
                draw.rectangle([(j * inside_box_size[0] + 200, i * 150 + 80), 
                              ((j + 1) * inside_box_size[0] + 200, (i + 1) * 150 + 80)], 
                             fill=random_color(), outline="black")
            else:
                draw.rectangle([(j * inside_box_size[0] + 200, i * 150 + 80), 
                              ((j + 1) * inside_box_size[0] + 200, (i + 1) * 150 + 80)], 
                             fill="white", outline="black")
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), "Lunch Break", 
                         fill="black", font=inside_font)
                continue

            # Add course information based on slot mapping
            slot_info = get_slot_info(i, j, section, roll_number)
            if slot_info:
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), slot_info["course"], 
                         fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), slot_info['type'], 
                         fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), slot_info.get('venue', ''),
                         fill="black", font=inside_font)

    # Add footer information
    draw.text((10, 1135), f"Roll Number: {roll_number}", fill="black", 
              font=ImageFont.load_default().font_variant(size=inside_font_size))
    draw.text((1350, 1135), "https://github.com/Naveen-Pal/1-timetable", fill="black", 
              font=ImageFont.load_default().font_variant(size=inside_font_size))
    draw.text((40, 20), "IITGN", fill="black", font=inside_font)
    
    # Save the timetable
    timetable_image.save(f"{roll_number}.png")

def get_slot_info(time_slot, day, section, roll_number):
    # Slot mapping (time_slot, day) -> slot code
    slot_mapping = {
        (0, 0): "A1", (0, 1): "B1", (0, 2): "A2", (0, 3): "C2", (0, 4): "B2",
        (1, 0): "C1", (1, 1): "D1", (1, 2): "E1", (1, 3): "D2", (1, 4): "E2",
        (2, 0): "F1", (2, 1): "G1", (2, 2): "H2", (2, 3): "F2", (2, 4): "G2",
        (3, 0): "T1", (3, 1): "T2", (3, 2): "T3", (3, 3): "O1", (3, 4): "O2",
        (4, 0): "I1", (4, 1): "J1", (4, 2): "I2", (4, 3): "K2", (4, 4): "J2",
        (5, 0): "K1", (5, 1): "L1", (5, 2): "M1", (5, 3): "L2", (5, 4): "M2",
        (6, 0): "H1", (6, 1): "N1", (6, 2): "P1", (6, 3): "N2", (6, 4): "P2"
    }

    # Course mapping based on slots
    course_mapping = {
        "A1": {"type": "Tutorial", "course": "Calculus", "venue": "AB 7"},
        "B1": {"type": "Lab", "course": "Writing", "venue": "AB 7"},
        "B2": {"type": "Lab", "course": "Writing", "venue": "AB 7"},
        "C1": {"type": "Lecture", "course": "DIP", "venue": "Jasubhai Auditorium"},
        "C2": {"type": "Lecture", "course": "Eng Graphics", "venue": "Jasubhai Auditorium"},
        "E1": {"type": "Lecture", "course": "Calculus", "venue": "Jasubhai Auditorium"},
        "E2": {"type": "Lecture", "course": "Calculus", "venue": "Jasubhai Auditorium"},
        "F1": {"type": "Lecture", "course": "Computing", "venue": "Jasubhai Auditorium"},
        "H1": {"type": "Lab", "course": "Writing", "venue": "AB 7"},
        "H2": {"type": "Lab", "course": "Writing", "venue": "AB 7"},
        "N1": {"type": "Lab", "course": "Eng Graphics", "venue": "Surendra LT"},
        "N2": {"type": "Lab", "course": "Eng Graphics", "venue": "Surendra LT"},
        "P1": {"type": "Lab", "course": "Computing", "venue": "AB 10"},
        "P2": {"type": "Lab", "course": "Computing", "venue": "AB 10"}
    }

    # DIP Lab slots based on section
    dip_lab_slots = {
        1: [("I1", "K1")],
        2: [("J1", "L1")],
        3: [("I2", "M1")],
        4: [("K2", "L2")],
        5: [("J2", "M2")]
    }

    # BS 192 Lab slots based on section and roll number ranges
    bs192_lab_slots = {
        1: [("K2", "L2")],
        2: [("I2", "M1")],
        3: [("J1", "L1")],
        4: [("I1", "K1")],
        5: {  # Multiple slots based on roll number ranges
            (25110289, 25110306): [("I1", "K1")],
            (25110307, 25110325): [("J1", "L1")],
            (25110326, 25110343): [("I2", "M1")],
            (25110344, 25110361): [("K2", "L2")]
        }
    }

    slot_code = slot_mapping.get((time_slot, day))
    if not slot_code:
        return None

    # Check if it's a BS 192 lab slot for the student's section
    if section == 5:
        # For section 5, check roll number ranges
        for roll_range, slots in bs192_lab_slots[5].items():
            if roll_range[0] <= roll_number <= roll_range[1]:
                if slot_code in [s for pair in slots for s in pair]:
                    return {"type": "Lab", "course": "BS 192", "venue": "PH Lab"}
    else:
        # For sections 1-4, check the slots directly
        section_slots = bs192_lab_slots.get(section, [])
        if slot_code in [s for pair in section_slots for s in pair]:
            return {"type": "Lab", "course": "BS 192", "venue": "PH Lab"}

    # Check if it's a DIP lab slot for the student's section
    for section_slots in dip_lab_slots.get(section, []):
        if slot_code in section_slots:
            return {"type": "Lab", "course": "DIP", "venue": "Surendra LT"}

    return course_mapping.get(slot_code, {"type": "Free", "course": "", "venue": ""})

if __name__ == "__main__":
    student_roll_number = 25110001
    inside_font_size = 32
    inside_box_size = (350, 75)
    
    while student_roll_number <= 25110361:
        generate_timetable(student_roll_number, inside_font_size, inside_box_size)
        # print(f"Generated timetable for roll number {student_roll_number}")
        student_roll_number += 1
    
    print("All timetables have been generated and saved to current working folder")
