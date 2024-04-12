
#!/usr/bin/python3

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
        "Tell me about the INAUGURATION CEREMONY": "The INAUGURATION CEREMONY starts at 9:00 AM on April 25 and ends at 11:00 AM.",
        "Tell me about the NON-PROTOTYPE PROJECT DISPLAY": "The NON-PROTOTYPE PROJECT DISPLAY starts at 11:00 AM on April 25 and ends at 12:30 PM.",
        "Tell me about the EXTEMPORE SPEECH": "The EXTEMPORE SPEECH starts at 12:30 PM on April 25 and continues onwards.",
        "Tell me about the FOOD BREAK": "The FOOD BREAK starts at 1:30 PM and ends at 2:30 PM.",
        "Tell me about the Truss Challenge": "The Truss Challenge starts at 2:30 PM on April 25 and ends at 6:00 PM.",
        "Tell me about the PROJECT DISPLAY": "The PROJECT DISPLAY starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "Tell me about the SCRAPBOOK DISPLAY": "The SCRAPBOOK DISPLAY starts at 9:00 AM on April 26 and ends at 5:30 PM.",
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
        "who is Mehedi Ahamed": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "who is Mehdi Ahamed": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "who is Mehdi Aamed": "I was created by Mehedi Ahamed. A CSE grad currently studying in Islamic University of Technology. He is an ex josphite, batch-18. You can follow Mehedi Ahamed on Facebook and Instagram",
        "Tell me about the EXHIBITIONS ": "The EXHIBITION (ROBOTS, WALL MAGAZINE, ARTWORK, POSTER) starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "Tell me about the ROBOTICS ": "The ROBOTICS (Robo Soccer, Robo War, Line Following Robot, Cyberspace) starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "Tell me about the SCI-FI BOOK BASED QUIZ": "The SCI-FI BOOK BASED QUIZ PRELIMINARY starts at 9:00 AM on April 26 and ends at 9:30 AM. The SCI-FI BOOK BASED QUIZ FINAL starts at 2:15 PM on April 26 and ends at 3:15 PM.",
        "Tell me about the SCI-FI MOVIE BASED QUIZ": "The SCI-FI MOVIE BASED QUIZ starts at 9:45 AM on April 26 and ends at 10:15 AM. The SCI-FI MOVIE BASED QUIZ FINAL starts at 11:00 AM on April 27 and ends at 12:00 PM.",
        "Tell me about the ANIME QUIZ": "The ANIME QUIZ starts at 10:30 AM on April 26 and ends at 11:00 AM. The ANIME QUIZ FINAL starts at 12:15 PM on April 27 and ends at 1:15 PM.",
        "Tell me about the GENERAL KNOWLEDGE QUIZ": "The GENERAL KNOWLEDGE QUIZ starts at 11:15 AM on April 26 and ends at 11:45 AM. The GENERAL KNOWLEDGE QUIZ FINAL starts at 3:30 PM on April 26 and ends at 4:30 PM.",
        "Tell me about the MARVEL VS DC QUIZ": "The MARVEL VS DC QUIZ starts at 12:00 PM on April 26 and ends at 1:00 PM. The MARVEL VS DC QUIZ FINAL starts at 1:30 PM on April 27 and ends at 2:30 PM.",
        "Tell me about the MEGA QUIZ": "The MEGA QUIZ starts at 4:30 PM on April 26 and continues onwards.",
        "Tell me about the PROJECT JUDGEMENT": "The PROJECT JUDGEMENT starts at 8:30 AM on April 27 and continues onwards.",
        "Tell me about the CLOSING CEREMONY": "The CLOSING CEREMONY starts at 2:30 PM on April 27 and ends at 6:00 PM.",
        "INAUGURATION CEREMONY": "The INAUGURATION CEREMONY starts at 9:00 AM on April 25 and ends at 11:00 AM.",
        "NON-PROTOTYPE PROJECT DISPLAY": "The NON-PROTOTYPE PROJECT DISPLAY starts at 11:00 AM on April 25 and ends at 12:30 PM.",
        "EXTEMPORE SPEECH": "The EXTEMPORE SPEECH starts at 12:30 PM on April 25 and continues onwards.",
        "FOOD BREAK": "The FOOD BREAK starts at 1:30 PM and ends at 2:30 PM.",
        "Truss Challenge": "The Truss Challenge starts at 2:30 PM on April 25 and ends at 6:00 PM.",
        "PROJECT DISPLAY": "The PROJECT DISPLAY starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "SCRAPBOOK DISPLAY": "The SCRAPBOOK DISPLAY starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "EXHIBITIONS ": "The EXHIBITION (ROBOTS, WALL MAGAZINE, ARTWORK, POSTER) starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "ROBOTICS ": "The ROBOTICS (Robo Soccer, Robo War, Line Following Robot, Cyberspace) starts at 9:00 AM on April 26 and ends at 5:30 PM.",
        "SCI-FI BOOK BASED QUIZ": "The SCI-FI BOOK BASED QUIZ PRELIMINARY starts at 9:00 AM on April 26 and ends at 9:30 AM. The SCI-FI BOOK BASED QUIZ FINAL starts at 2:15 PM on April 26 and ends at 3:15 PM.",
        "SCI-FI MOVIE BASED QUIZ": "The SCI-FI MOVIE BASED QUIZ starts at 9:45 AM on April 26 and ends at 10:15 AM. The SCI-FI MOVIE BASED QUIZ FINAL starts at 11:00 AM on April 27 and ends at 12:00 PM.",
        "ANIME QUIZ": "The ANIME QUIZ starts at 10:30 AM on April 26 and ends at 11:00 AM. The ANIME QUIZ FINAL starts at 12:15 PM on April 27 and ends at 1:15 PM.",
        "GENERAL KNOWLEDGE QUIZ": "The GENERAL KNOWLEDGE QUIZ starts at 11:15 AM on April 26 and ends at 11:45 AM. The GENERAL KNOWLEDGE QUIZ FINAL starts at 3:30 PM on April 26 and ends at 4:30 PM.",
        "MARVEL VS DC QUIZ": "The MARVEL VS DC QUIZ starts at 12:00 PM on April 26 and ends at 1:00 PM. The MARVEL VS DC QUIZ FINAL starts at 1:30 PM on April 27 and ends at 2:30 PM.",
        "MEGA QUIZ": "The MEGA QUIZ starts at 4:30 PM on April 26 and continues onwards.",
        "PROJECT JUDGEMENT": "The PROJECT JUDGEMENT starts at 8:30 AM on April 27 and continues onwards.",
        "CLOSING CEREMONY": "The CLOSING CEREMONY starts at 2:30 PM on April 27 and ends at 6:00 PM.",
        
        
       }
    responses = {key.lower(): value for key, value in responses.items()}

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



