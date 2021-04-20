import pandas as pd
import time
from bs4 import BeautifulSoup as bs
import bs4
import urllib.request as req
import io

#node class representing a player
class Node:
    def __init__(self,my_id,my_name):
        self.id = my_id
        self.name = my_name
        self.adj = set()


fout = io.open('graph.txt','w',encoding='utf-8')
#list of NBA teams
teams = ['BOS','NJN','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOH','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']

#given a url to a roster page, this function returns an array of tuples with player ids and names
def getRoster(url):
    page = req.urlopen(url)
    soup = bs(page,features='lxml')
    table = soup.find_all('div',{'id':'div_roster'})
    roster = []

    for child in table[0].children:
        if(type(child)==bs4.element.Tag):
            team = child.contents[7].contents
            for i in range(0,len(team),2):
                id = team[i].contents[1].contents[0]['href']
                name = team[i].contents[1].contents[0].contents[0]
                roster.append((str(id),str(name)))
    return roster

#given a team id, this function returns an array of URLs to each of the team's yearly rosters
def getTeamUrls(team):
    url = 'https://www.basketball-reference.com/teams/'+str(team)
    page = req.urlopen(url)
    soup = bs(page,features='lxml')
    table = soup.find_all('th',{'class':'left'})
    urls = []
    for dir in table:
        urls.append('https://www.basketball-reference.com'+dir.contents[0]['href'])
    return urls

#returns the graph with players as nodes and being on the same roster as edges
def makeGraph():
    graph = {}
    for team in teams:
        urls = getTeamUrls(team)
        for url in urls:
            roster = getRoster(url)
            for p1 in roster:
                for p2 in roster:
                    if p1[0] != p2[0]:
                        if p1[0] not in graph:
                            graph[p1[0]] = Node(p1[0],p1[1])
                        graph[p1[0]].adj.add(p2[0])
        print(team)
    return graph
getRoster('https://www.basketball-reference.com/teams/BOS/2020.html')
graph = makeGraph()

#writes the graph to graph.txt
fout.write(str(len(graph)) + '\n')
for player1 in graph:
    fout.write( graph[player1].id+'\n' )
    fout.write( graph[player1].name+'\n' )
    fout.write( str( len(graph[player1].adj) ) + '\n')
    for player2 in graph[player1].adj:
        fout.write(player2+'\n')