from presentation_futuristic import create_slides_futuristic
from presentation_galaxy import create_slides_galaxy
from presentation_historical import create_slides_historical
from chat import chat_with_gpt
from presentation_cyberpunk import create_slides_cyberpunk
from presentation_landscape import create_slides_landscape
from presentation_cube import create_slides_cube
from gui import gui

google_api_key = "AIzaSyBJnQIS_XMOdax8WtjKROG20pgCANHMw0U"
google_search_engine_id = "f6d5812a377554523"

def answer(response):
    print(response)

    topic = response[0]
    pic = response[1]
    slide_number = response[2]
    template = response[3]
    choice = response[4]
    slide_title = []
    if choice == 1:
        for i in range(slide_number):
            slide_title.append(response[i+5])
    if template == 5:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_cyberpunk(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 6:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_landscape(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 1:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_cube(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 2:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_futuristic(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 3:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_galaxy(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 4:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_historical(gpt_response, slide_title, slide_number, topic, choice, pic)
    else:
        print("error")

gui(answer)    