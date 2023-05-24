import requests
from bs4 import BeautifulSoup


def process_link(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    questions = []
    name = ""
    hall_ticket_number = ""
    for question in soup.find_all("div", class_="question-pnl"):
        questions.append(question)
    score = 0
    for question in questions:
        correct_option = int(question.find("td", class_="rightAns").text[0])
        chosen_option = int(question.find_all("td", class_="bold")[-1].text)
        if correct_option == chosen_option:
            score += 1
    target_name = soup.find("td", text="Hall Ticket Number")
    hall_ticket_number = target_name.find_next_sibling().text
    target_hall_ticket = soup.find("td", text="Participant Name")
    name = target_hall_ticket.find_next_sibling().text
    return [score, name, hall_ticket_number]
