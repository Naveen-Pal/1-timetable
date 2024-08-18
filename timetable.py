import random
from PIL import Image, ImageDraw, ImageFont

def generate_colorful_timetable(roll_number, inside_font_size=12, inside_box_size=(200, 70)):
    def random_color():
        return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    roll_number=int(roll_number)
    if not 24110001 <= roll_number <= 24110404:
        print("wrong Roll Number")
        exit(1)

    # Increased size of the timetable image
    timetable_image = Image.new('RGB', (2000, 1200), color='white')
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
    days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday"]

    # Draw headers with white background
    for i, day in enumerate(days):
        draw.rectangle([(i * inside_box_size[0] + 200, 0), ((i + 1) * inside_box_size[0] + 200, 80)], fill="white", outline="black")
        draw.text((i * inside_box_size[0] + 240, 20), day, fill="black", font=font_large)

    rn=roll_number-24110000
    if rn<81:
        section=1
    elif rn<164:
        section=2
    elif rn<241:
        section=3
    elif rn<323:
        section=4
    elif rn<405:
        section=5

    for i, time_slot in enumerate(time_slots):
        draw.rectangle([(0, i * 150 + 80), (200, (i + 1) * 150 + 80)], fill="white", outline="black")
        draw.text((20, i * 150 + 110), time_slot, fill="black", font=font_large)
        # Add text based on the venue and class details with colorful background
        for j, day in enumerate(days):
            box_size = (
                inside_box_size[0],  # Width of the box
                inside_box_size[1]  # Height of the box based on the number of lines
            )
            if i==3:
                draw.rectangle([(j * inside_box_size[0] + 200, i * 150 + 80), ((j + 1) * inside_box_size[0] + 200, (i + 1) * 150 + 80)], fill="white",outline="black")
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lunch Break", fill="black", font=inside_font)
                continue
                
            else:
                draw.rectangle([(j * inside_box_size[0] + 200, i * 150 + 80), ((j + 1) * inside_box_size[0] + 200, (i + 1) * 150 + 80)], fill=random_color(),outline="black")

            if (i,j)==(0,0):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"Data Visualization", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)           
            
            elif (i,j)==(0,1) or (i,j)==(0,4):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Calculus", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)     

            #check lecture lab or tutorial
            elif (i,j)==(0,2):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)

            elif (i,j)==(0,3) or (i,j) =(1,0) :
                if not ((rn>=226 and rn<=262) or (rn>=152 and rn<=188)):
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Writing ", fill="black", font=inside_font)
                    # if rn<40:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/101", fill="black", font=inside_font)
                    # elif rn<78:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/210", fill="black", font=inside_font)
                    # elif rn<115:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/103", fill="black", font=inside_font)
                    # elif rn<152:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/104", fill="black", font=inside_font) 
                    # elif rn<189:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 10/101, 7/107", fill="black", font=inside_font)
                    # elif rn<226:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/105", fill="black", font=inside_font)
                    # elif rn<263:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/107", fill="black", font=inside_font) 
                    # elif rn<299:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/110", fill="black", font=inside_font)
                    # elif rn<336:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/201", fill="black", font=inside_font)
                    # elif rn<374:
                    #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/204", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            # elif (i,j)==(0,4):
            #     if rn<400 and rn>=200:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Probability statistics and", fill="black", font=inside_font)
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"Data Visualization", fill="black", font=inside_font)
            #         if rn<250:
            #             draw.text((j * inside_box_size[0] + 240, i * 150 + 190), f"venue: 7/109", fill="black", font=inside_font)
            #         elif rn<350:
            #             draw.text((j * inside_box_size[0] + 240, i * 150 + 190), f"venue: 1/101", fill="black", font=inside_font)
            #         elif rn<400:
            #             draw.text((j * inside_box_size[0] + 240, i * 150 + 190), f"venue: 1/102", fill="black", font=inside_font)
            #     else:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(1,1):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"WCC", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"And Cultures", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(1,2):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Engineering Graphics", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(1,3):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"WCC", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"And Cultures", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(1,4):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials For Future", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(2,0):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)

            elif (i,j)==(2,2):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                
            elif (i,j)==(2,3):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Computing", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"Electrical Engineering", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(2,4) or (i,j)==(2,1):

            # if not ((rn>=226 and rn<=262) or (rn>=152 and rn<=188)):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Writing ", fill="black", font=inside_font)
            #     if rn<40:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/101", fill="black", font=inside_font)
            #     elif rn<78:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/210", fill="black", font=inside_font)
            #     elif rn<115:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/103", fill="black", font=inside_font)
            #     elif rn<152:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/104", fill="black", font=inside_font) 
            #     elif rn<189:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 10/101, 7/107", fill="black", font=inside_font)
            #     elif rn<226:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/105", fill="black", font=inside_font)
            #     elif rn<263:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/107", fill="black", font=inside_font) 
            #     elif rn<299:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/110", fill="black", font=inside_font)
            #     elif rn<336:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/201", fill="black", font=inside_font)
            #     elif rn<374:
            #         draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/204", fill="black", font=inside_font)
            # else:
            #     draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
        
            elif (i,j)==(4,0):
                if section==1:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(4,1):
                if section==2:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(4,2):
                if section==3:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
            elif (i,j)==(4,3):
                if section==4:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                
            elif (i,j)==(4,4):
                if section==5:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
            elif (i,j)==(5,0):
                if section==1:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                elif section==5:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: MSE Lab", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(5,1):
                if section==2:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                elif section==4:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: MSE Lab", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(5,2):
                if section==3:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                elif section==2:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: MSE Lab", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
            elif (i,j)==(5,3):
                if section==4:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                elif section==3:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: MSE Lab", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                
            elif (i,j)==(5,4):
                if section==5:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"DIP", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 1/101", fill="black", font=inside_font)
                elif section==1:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Materials", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: MSE Lab", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
                    
            elif (i,j)==(6,0):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Tutorial", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Calculus", fill="black", font=inside_font)
                # if rn<44:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/101", fill="black", font=inside_font)
                # elif rn<85:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/210", fill="black", font=inside_font)
                # elif rn<126:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/103", fill="black", font=inside_font)
                # elif rn<167:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/104", fill="black", font=inside_font) 
                # elif rn<209:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/105", fill="black", font=inside_font)
                # elif rn<250:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/110", fill="black", font=inside_font)
                # elif rn<290:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/201", fill="black", font=inside_font) 
                # elif rn<332:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/204", fill="black", font=inside_font)
                # elif rn<374:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/205", fill="black", font=inside_font)
                    
            elif (i,j)==(6,1) or (i,j)==(6,3):
                # if section==1 or section==2:
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Engineering Graphics", fill="black", font=inside_font)
                # if rn<200:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/108", fill="black", font=inside_font)
                # else:
                #     draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/109", fill="black", font=inside_font)
                    
            elif (i,j)==(6,2) or (i,j)==(6,4):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lab", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Computing", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: 7/108 or 7/109", fill="black", font=inside_font)
    
        timetable_image.save(str(roll_number)+'.png')

            
if __name__ == "__main__":
    student_roll_number = int(input("Enter Your Roll Number: "))
    inside_font_size = 32  # Set the desired font size for inside text
    inside_box_size = (350, 75)  # Set the desired box size for inside text
    generate_colorful_timetable(student_roll_number, inside_font_size, inside_box_size)
    print("Your TimeTable has been saved to current working folder")
