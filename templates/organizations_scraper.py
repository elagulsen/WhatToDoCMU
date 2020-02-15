# import HTMLSession from requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#page_number < 40 but ideally less than like, 10
def organization_scraper(page_number):
    session = HTMLSession()
    new_orgs = dict()
    for i in range(page_number):
        if i == 0:
            url = "https://thebridge.cmu.edu/api/discovery/search/organizations?orderBy[0]=UpperName%20asc&top=10&filter=&query=&skip=0"
        else:
            url = "https://thebridge.cmu.edu/api/discovery/search/organizations?orderBy[0]=UpperName%20asc&top=10&filter=&query=&skip=" + str(i*10)
        resp = session.get(url)
        resp.html.render()

        orgs = []
        index = 0
        for element in resp.html.html.split('{'):
            orgs.append([])
            for data in element.split(','):
                orgs[index].append(data)
            index += 1
        #print(orgs)

        for element in orgs:
            is_org = False
            category = None
            summary_seen = False
            summary = ''
            for data in element:
                if "CategoryNames" in data:
                    category = data.split(":")[1].strip('[]"')
                elif "Name" in data:
                    is_org = True
                    name = (data.split(":")[1]).strip('"').replace("&amp;", "&")
                elif "CategoryIds" in data:
                    summary_seen = False
                elif "WebsiteKey" in data:
                    website = "https://thebridge.cmu.edu/organization/" + (data.split(":")[1]).strip('"')
                if summary_seen:
                    summary += data
                elif "Summary" in data:
                    summary_seen = True
                    summary += (data.split(":")[1]).strip('"')
                if category and summary and name and is_org:
                    new_orgs[name] = dict()
                    new_orgs[name]["category"] = category
                    new_orgs[name]["website"] = website
                    new_orgs[name]["summary"] = summary
    return new_orgs

organization_scraper(2)
