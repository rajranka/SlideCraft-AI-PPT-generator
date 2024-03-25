import openai

openai.api_key = "paste your key here"

def chat_with_gpt(topic, slide_number,slide_title, choice):
    dct=[]
    result=[]
    print("started\n\n")
    # loading()

    if choice == 1:
        if slide_number == 3:
            prompt = "I am giving you a Topic : "+topic+" and 3 Subtopics : "+slide_title[0]+" , "+slide_title[1]+" , "+slide_title[2]+" return a short description consisting only information about every subtopic, very strictly follow the given syntax - Summary 1 : description , Summary 2 : description , Summary 3 : description"
        if slide_number == 6:
            prompt = "I am giving you a Topic : "+topic+" and 6 Subtopics : "+slide_title[0]+" , "+slide_title[1]+" , "+slide_title[2]+" , "+slide_title[3]+" , "+slide_title[4]+" , "+slide_title[5]+" return a short description consisting only information about every subtopic, very strictly follow the given syntax - Summary 1 : description , Summary 2 : description , Summary 3 : description , Summary 4 : description , Summary 5 : description , Summary 6 : description"
        if slide_number == 9:
            prompt = "I am giving you a Topic : "+topic+" and 9 Subtopics : "+slide_title[0]+" , "+slide_title[1]+" , "+slide_title[2]+" , "+slide_title[3]+" , "+slide_title[4]+" , "+slide_title[5]+" , "+slide_title[6]+" , "+slide_title[7]+" , "+slide_title[8]+" return a short description consisting only information about every subtopic, very strictly follow the given syntax - Summary 1 : description , Summary 2 : description , Summary 3 : description , Summary 4 : description , Summary 5 : description , Summary 6 : description , Summary 7 : description , Summary 8 : description , Summary 9 : description"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [{"role": "system", "content" : prompt}]
        )
        ans = response.choices[0].message.content
        dct = ans.strip().split('\n\n')
        for i in range(len(dct)):
            result.append(dct[i])
        # load = loading_kill()
        return result

    elif choice == 2:
        if slide_number == 3:
            prompt = "This is a Topic : "+topic+". Generate 3 relevant subtopics and a short description consisting only information about every subtopic, very strictly follow the given syntax and do not change the syntax even slightly - Subtopic 1 : 'replace this with subtopic 1'-description: 'replace this with description 1'-Subtopic 2 : 'replace this with subtopic 2'-description: 'replace this with description 2'-Subtopic 3 : 'replace this with subtopic 3'-description: 'replace this with description 3'"
        if slide_number == 6:
            prompt = "I am giving you a Topic : "+topic+". Generate 6 relevant subtopics and return a short description consisting only information about every subtopic, very strictly follow the given syntax do not change the syntax even slightly - Subtopic 1 : 'replace this with subtopic 1'-description: 'replace this with description 1'-Subtopic 2 : 'replace this with subtopic 2'-description: 'replace this with description 2'-Subtopic 3 : 'replace this with subtopic 3'-description: 'replace this with description 3'-Subtopic 4 : 'replace this with subtopic 4'-description: 'replace this with description 4'-Subtopic 5 : 'replace this with subtopic 5'-description: 'replace this with description 5'-Subtopic 6 : 'replace this with subtopic 6'-description: 'replace this with description 6'"
        if slide_number == 9:
            prompt = "I am giving you a Topic : "+topic+". Generate 9 relevant subtopics and return a short description consisting only information about every subtopic, very strictly follow the given syntax and only replace subtopic and description with the generated responses - Subtopic 1 : 'replace this with subtopic 1'-description: 'replace this with description 1'-Subtopic 2 : 'replace this with subtopic 2'-description: 'replace this with description 2'-Subtopic 3 : 'replace this with subtopic 3'-description: 'replace this with description 3'-Subtopic 4 : 'replace this with subtopic 4'-description: 'replace this with description 4'-Subtopic 5 : 'replace this with subtopic 5'-description: 'replace this with description 5'-Subtopic 6 : 'replace this with subtopic 6'-description: 'replace this with description 6'-Subtopic 7 : 'replace this with subtopic 7'-description: 'replace this with description 7'-Subtopic 8 : 'replace this with subtopic 8'-description: 'replace this with description 8'-Subtopic 9 : 'replace this with subtopic 9'-description: 'replace this with description 9'"
        print("sent\n\n")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [{"role": "system", "content" : prompt}]
        )
        ans = response.choices[0].message.content
        dct = ans.strip().split('\n\n')
        for i in range(len(dct)):
            result.append(dct[i])
        print("\n\nResponse GPT given\n\n")
        # loading_kill()
        return result