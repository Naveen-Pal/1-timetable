import random
from PIL import Image, ImageDraw, ImageFont

def generate_colorful_timetable(roll_number, inside_font_size=12, inside_box_size=(200, 70)):
    def random_color():
        return (random.randint(200, 255), random.randint(100, 255), random.randint(100, 255))
    roll_number=int(roll_number)
    if not 24110001 <= roll_number <= 24110404:
        print("wrong Roll Number")
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
    days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday"]

    # Draw headers with white background
    for i, day in enumerate(days):
        draw.rectangle([(i * inside_box_size[0] + 200, 0), ((i + 1) * inside_box_size[0] + 200, 80)], fill="white", outline="black")
        draw.text((i * inside_box_size[0] + 240, 20), day, fill="black", font=font_large)
    hs = 0
    if roll_number in [
        24110017, 24110022, 24110029, 24110031, 24110040, 24110044, 24110051, 24110052, 
        24110053, 24110060, 24110064, 24110067, 24110068, 24110072, 24110074, 24110081, 
        24110083, 24110087, 24110090, 24110091, 24110096, 24110100, 24110111, 24110114, 
        24110118, 24110126, 24110135, 24110153, 24110166, 24110185, 24110187, 24110189,
        21110241, 24110001, 24110003, 24110004, 24110005, 24110006, 24110007, 24110009, 
        24110010, 24110011, 24110012, 24110013, 24110014, 24110015, 24110016, 24110018, 
        24110019, 24110020, 24110021, 24110023, 24110024, 24110025, 24110026, 24110027, 
        24110028, 24110030, 24110032, 24110033, 24110034, 24110035, 24110036, 24110037, 
        24110038, 24110039, 24110041, 24110042, 24110043, 24110045, 24110046, 24110047,
        24110048, 24110049, 24110050, 24110054, 24110055, 24110056, 24110057, 24110058, 
        24110059, 24110061, 24110062, 24110063, 24110065, 24110066, 24110069, 24110070, 
        24110071, 24110073, 24110075, 24110076, 24110077, 24110078, 24110079, 24110080, 
        24110082, 24110084, 24110085, 24110086, 24110088, 24110089, 24110092, 24110093, 
        24110094, 24110095, 24110097, 24110098, 24110101, 24110103, 24110104, 24110105,
        24110106, 24110107, 24110108, 24110109, 24110110, 24110112, 24110113, 24110115, 
        24110116, 24110117, 24110119, 24110120, 24110121, 24110122, 24110123, 24110124, 
        24110125, 24110127, 24110128, 24110129, 24110130, 24110131, 24110132, 24110133, 
        24110134, 24110136, 24110138, 24110139, 24110140, 24110141, 24110143, 24110144, 
        24110145, 24110146, 24110147, 24110148, 24110149, 24110151, 24110152, 24110154
    ]:
        hs = 1
    elif roll_number in [
        24110190, 24110191, 24110207, 24110214, 24110217, 24110233, 24110253, 24110258, 
        24110261, 24110264, 24110265, 24110271, 24110279, 24110284, 24110285, 24110297, 
        24110299, 24110302, 24110311, 24110321, 24110322, 24110340, 24110360, 24110362, 
        24110363, 24110372, 24110375, 24110387, 24110388, 24110392, 24110395,
        24110155, 24110157, 24110158, 24110159, 24110160, 24110161, 24110162, 24110163, 
        24110164, 24110165, 24110167, 24110168, 24110169, 24110170, 24110171, 24110172, 
        24110174, 24110175, 24110176, 24110177, 24110178, 24110179, 24110180, 24110181, 
        24110182, 24110183, 24110184, 24110186, 24110188, 24110192, 24110193, 24110194, 
        24110195, 24110196, 24110197, 24110198, 24110199, 24110200, 24110201, 24110202,
        24110203, 24110204, 24110205, 24110206, 24110208, 24110209, 24110210, 24110211, 
        24110212, 24110213, 24110215, 24110216, 24110218, 24110219, 24110220, 24110221, 
        24110222, 24110223, 24110224, 24110225, 24110226, 24110227, 24110228, 24110229, 
        24110230, 24110231, 24110232, 24110234, 24110235, 24110236, 24110237, 24110238, 
        24110239, 24110240, 24110241, 24110242, 24110243, 24110245, 24110246, 24110247
    ]:
        hs=2
    elif roll_number in [
        24110248, 24110249, 24110250, 24110251, 24110252, 24110254, 24110255, 24110256, 
        24110257, 24110259, 24110260, 24110262, 24110263, 24110266, 24110268, 24110269, 
        24110270, 24110272, 24110274, 24110275, 24110276, 24110277, 24110278, 24110280, 
        24110281, 24110282, 24110283, 24110286, 24110287, 24110288, 24110289, 24110290, 
        24110291, 24110293, 24110294, 24110295, 24110296, 24110298, 24110300, 24110301,
        24110303, 24110304, 24110305, 24110307, 24110308, 24110309, 24110310, 24110312, 
        24110313, 24110314, 24110315, 24110316, 24110317, 24110318, 24110319, 24110320, 
        24110323, 24110324, 24110325, 24110326, 24110327, 24110328, 24110329, 24110330, 
        24110331, 24110332, 24110333, 24110334, 24110335, 24110336, 24110337, 24110339, 
        24110341, 24110342, 24110343, 24110344, 24110345, 24110346, 24110348, 24110349,
        24110350, 24110351, 24110352, 24110353, 24110354, 24110356, 24110357, 24110358, 
        24110361, 24110364, 24110365, 24110366, 24110367, 24110368, 24110369, 24110370, 
        24110371, 24110373, 24110374, 24110376, 24110377, 24110378, 24110379, 24110380, 
        24110381, 24110382, 24110383, 24110384, 24110385, 24110386, 24110389, 24110390, 
        24110391, 24110393, 24110394, 24110396, 24110397, 24110398, 24110399, 24110400, 
        24110401, 24110402, 24110403, 24110404
    ]:
        hs = 3
    else:
        hs =1

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

            elif (i,j)==(0,3) or (i,j) ==(1,0) :
                if hs==2:
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
            elif (i,j)==(2,0) or (i,j)==(2,2):
                if hs==3:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Writing ", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)

            elif (i,j)==(2,3):
                draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Computing", fill="black", font=inside_font)
                # draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"Electrical Engineering", fill="black", font=inside_font)
                draw.text((j * inside_box_size[0] + 240, i * 150 + 170), f"venue: Jasubhai", fill="black", font=inside_font)
            elif (i,j)==(2,4) or (i,j)==(2,1):

                if hs==1:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Lecture", fill="black", font=inside_font)
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 140), f"Writing ", fill="black", font=inside_font)
                else:
                    draw.text((j * inside_box_size[0] + 240, i * 150 + 110), f"Free", fill="black", font=inside_font)
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


        draw.text((10, 1135), f"Roll Number: {roll_number}", fill="black", font=ImageFont.load_default().font_variant(size=inside_font_size))
        draw.text((1700, 1135), f"© 2024, Naveen", fill="black", font=ImageFont.load_default().font_variant(size=inside_font_size))
        draw.text((40, 20), f"IITGN", fill="black", font=inside_font)
        timetable_image.save(str(roll_number)+'.png')

            
if __name__ == "__main__":
    student_roll_number = int(input("Enter Your Roll Number: "))
    inside_font_size = 32  # Set the desired font size for inside text
    inside_box_size = (350, 75)  # Set the desired box size for inside text
    generate_colorful_timetable(student_roll_number, inside_font_size, inside_box_size)
    print("Your TimeTable has been saved to current working folder")
