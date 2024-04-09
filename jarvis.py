'''
pip install wikipedia speech_recognition pyttsx3
'''

import wikipedia
import speech_recognition as sr
import pyttsx3
import requests
import re

recognizer = sr.Recognizer()  # Speech recognizer
engine = pyttsx3.init()  # Text-to-speech engine

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def search_wiki(keyword=''):
#     try:
#         page = wikipedia.page(keyword)
#         wikiSummary = page.summary
#         # Split the summary by newline characters and return the first paragraph
#         summary_lines = wikiSummary.split('.')[:1]
#         return '.'.join(summary_lines)
#     except (wikipedia.DisambiguationError, wikipedia.PageError):
#         return None



def search_wiki(keyword):
    try:
        page = wikipedia.page(keyword)
        wiki_summary = page.summary
        # Split the summary by periods and return the first 3 sentences
        sentences = re.split(r'(?<=[.:;])\s', wiki_summary)
        first_three_sentences = ' '.join(sentences[:2])
        return first_three_sentences
    except (wikipedia.DisambiguationError, wikipedia.PageError):
        return None





# def search_google(query):
#     url = f"https://www.google.com/search?q={query}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, "html.parser")
#         search_results = soup.find_all("div", class_="tF2Cxc")
#         if search_results:
#             summary = search_results[0].text.strip()
#             return summary
#         else:
#             print("Error: Summary element not found in search results.")
#             return None
#     except Exception as e:
#         print("Error fetching search results:", e)
#         return None




def search_britannica(query):
    url = f"https://www.britannica.com/search?query={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_text = response.text
            # Find the index of the first occurrence of the snippet class
            start_index = html_text.find('mt-5 font-weight-normal')
            if start_index != -1:
                # Find the start and end indices of the paragraph within the snippet
                start_index = html_text.find('>', start_index) + 1
                end_index = html_text.find('</div>', start_index)
                # Extract the text of the first paragraph
                first_paragraph = html_text[start_index:end_index].strip()
                # sentences = re.split(r'(?<=[.:;])\s', first_paragraph)
                # first_three_sentences = ' '.join(sentences[:4])
                # return first_three_sentences

                return first_paragraph
                
            else:
                return None
        else:
            return None
    except Exception as e:
        print("Error accessing Britannica website or retrieving information:", e)
        return None





def answer_question(question):
    responses = {
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "I'm an AI assistant made by Mehedi Ahamed. You can call me Jarvis M 28.",
        "who are you": "I'm an AI assistant made by Mehedi Ahamed. You can call me Jarvis M 28.",

        "who created you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "who built you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "who made you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "ok jarvis who created you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "ok jarvis who built you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "ok jarvis who made you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "ok jarvis who built you": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "tell me about st joseph higher secondary school in dhaka": "St. Joseph Higher Secondary School stands out as one of the premier institutions of Bangladesh. The institution has accumulated an enviable fame in terms of outstanding performance of the students in the public exams as well as an overflow of students from around the country to accommodate to 100% passing rates with a very substantial number of GPA-5 over the years. A congenial atmosphere of the institution for teaching and learning has attracted people who value the essence of true education. St. Joseph opens doors for the students to open their eyes and minds as well as paves the way for making themselves complete and successful citizens.",
        "st joseph higher secondary school in dhaka": "St. Joseph Higher Secondary School stands out as one of the premier institutions of Bangladesh. The institution has accumulated an enviable fame in terms of outstanding performance of the students in the public exams as well as an overflow of students from around the country to accommodate to 100% passing rates with a very substantial number of GPA-5 over the years. A congenial atmosphere of the institution for teaching and learning has attracted people who value the essence of true education. St. Joseph opens doors for the students to open their eyes and minds as well as paves the way for making themselves complete and successful citizens.",
        "st joseph higher secondary school": "St. Joseph Higher Secondary School stands out as one of the premier institutions of Bangladesh. The institution has accumulated an enviable fame in terms of outstanding performance of the students in the public exams as well as an overflow of students from around the country to accommodate to 100% passing rates with a very substantial number of GPA-5 over the years. A congenial atmosphere of the institution for teaching and learning has attracted people who value the essence of true education. St. Joseph opens doors for the students to open their eyes and minds as well as paves the way for making themselves complete and successful citizens.",
        "what is the weather today": "I'm sorry, I don't have access to weather information at the moment.",
        "what is project altair": "Two former IUT MARS ROVER teams Anirban & Avijatrik combined to create Project Altair. Members of Project Altair formed IUT Robotics Society. Now this society has two projects- Project Altair (rover) & Project Aero (drone), both projects consist of robotic development enthusiast students of IUT.",
        "project altair": "Two former IUT MARS ROVER teams Anirban & Avijatrik combined to create Project Altair. Members of Project Altair formed IUT Robotics Society. Now this society has two projects- Project Altair (rover) & Project Aero (drone), both projects consist of robotic development enthusiast students of IUT.",
        "who is emon": "Mohammad Emon is an Electronical and Electronics Engineer and current Project Altair team lead. He is currently studying in Islamic University of Technology",
        "who is safwan sami": "Safwan Sami is an Electronical and Electronics Engineer and current Project Altair treasurer. He is currently studying in Islamic University of Technology",
    }

    if question.lower() in responses:
        answer = responses[question.lower()]
    else:
        try:
            answer = search_wiki(question)
            if(answer==None):
                answer =  search_britannica(question)
            if(answer==None):
                answer = "Sorry, I don't know an answer to that question."
        except wikipedia.DisambiguationError as e:
            answer =  search_britannica(question)
        except wikipedia.PageError:
            answer = "Sorry, I don't know an answer to that question."

    return answer





def listen():
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                speak("Listening")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
            
            print("Recognizing...")
            # speak("Recognizing")
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            speak("You said " + text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand. Please try again.")
            # speak("Sorry, I didn't understand. Please try again.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            print("Please try again.")
            # speak("Please try again.")
        finally:
            recognizer = sr.Recognizer()  



def main():
    speak("Hello, I am Jarvis-M 28! How can I assist you today?")
    while True:
        command = listen()

        if "exit" in command or "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            answer = answer_question(command)
            print("Answer:", answer)
            speak(answer)

if __name__ == "__main__":
    main()
