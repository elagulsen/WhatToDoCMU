# import HTMLSession from requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def calendar_scraper(option):
    session = HTMLSession()

    if option == "all":
        resp = session.get("https://thebridge.cmu.edu/events")
    elif option == "tomorrow":
        resp = session.get("https://thebridge.cmu.edu/events/?shortcutdate=tomorrow")
    elif option == "weekend":
        resp = session.get("https://thebridge.cmu.edu/events/?shortcutdate=this_weekend")
    else return

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
