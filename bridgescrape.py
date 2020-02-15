#! /usr/bin/python3

from requests_html import HTMLSession
from bs4 import BeautifulSoup

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def calendar_scraper(option):
    session = HTMLSession()

    if option == "all":
        resp = session.get("https://thebridge.cmu.edu/events")
    elif option == "tomorrow":
        resp = session.get("https://thebridge.cmu.edu/events/?shortcutdate=tomorrow")
    elif option == "weekend":
        resp = session.get("https://thebridge.cmu.edu/events/?shortcutdate=this_weekend")
    else:
        return

    resp.html.render()

    event_headers = resp.html.find("h3")
    event_info = resp.html.find("div")

    events = [line.text for line in event_headers]

    info = [line.text.split("\n") for line in event_info]

    new_info = []
    for i in info:
        if i not in new_info:
            new_info.append(i)
    info = new_info

    events = [events[i] for i in range(5,len(events))]

    add = False
    event_list = []
    for event in info[5]:
        if event == 'iCal FeedRSS Feed' or event == '(Showing 1-15 of 47)':
            add = False
        if event in events:
            add = True
            event_list.append([])
        if add:
            event_list[-1].append(event)

    return event_list

def convert_time(bad_time):
    time_list = bad_time.split(" ")
    correct_time = "2020-"
    if MONTHS.index(time_list[1]) < 10:
        correct_time += "0" + str(MONTHS.index(time_list[1]))
    else:
        correct_time += str(MONTHS.index(time_list[1]))
    correct_time += "-"
    correct_time += str(time_list[2])
    correct_time += "T"
    time_int = int(time_list[4].split(":")[0])
    if "AM" in time_list[4]:
        if time_int >= 10: 
            correct_time += time_list[4].replace("AM", "")
        else:
            correct_time += "0" + time_list[4].replace("AM", "")
    else:
        time_int += 12
        correct_time += str(time_int) + ":" + time_list[4].split(":")[1]
    return correct_time
print(calendar_scraper('all'))