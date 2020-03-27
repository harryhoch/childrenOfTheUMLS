import json
import requests


class UmlsApi:
    granting_ticket = ""
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username;
        self.password = password;
        self.setTgT()

    def setTgT(self):
        data = {'username': self.username, 'password': self.password}
        r = requests.post('https://utslogin.nlm.nih.gov/cas/v1/tickets', data)
        self.granting_ticket = r.headers['location'].rsplit('/', 1)[-1]
        # print(self.granting_ticket)

    def getSingleTicket(self):
        data = {'service': 'http://umlsks.nlm.nih.gov'}
        url = "https://utslogin.nlm.nih.gov/cas/v1/api-key/{0}".format(self.granting_ticket)
        # print(url)
        r = requests.post(url, data)
        return r.text

    def cuiSearch(self, cui):
        ticket = self.getSingleTicket()
        url = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{1}?ticket={0}".format(ticket, cui)
        #print(url)
        r = requests.get(url)
        # print r.text
        return r.text

    def getRelatedCuis(self, cui):
        cui_search_response_string = self.cuiSearch(cui)
        cui_search_response_json = json.loads(cui_search_response_string)
        # print(cui_search_response_json)

        cuis[cui] = cui_search_response_json['result']['name']

        ticket = self.getSingleTicket()
        relation_url = cui_search_response_json['result']['relations'] + "?/pageSize=1000&ticket={0}".format(ticket)
        # print(relation_url)
        relation_response_str = requests.get(relation_url).text
        Relation_response = json.loads(relation_response_str)

        for conceptRelation in relation_response['result']:
            if conceptRelation['relationLabel'] == 'RB':
                relatedCui = conceptRelation['relatedId'].rsplit('/', 1)[-1]                    
                print("recursing on .."+relatedCui)
                subcuis = self.getRelatedCuis(relatedCui)
                cuis = {**cuis,**subcuis}
        return cuis
