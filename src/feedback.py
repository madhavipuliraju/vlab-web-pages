from bs4 import BeautifulSoup
import sys
experimentfile=raw_input()
f=open(experimentfile,'r')
srchtml=f.read()
print srchtml
f.close()
soup = BeautifulSoup(srchtml, 'html.parser')
sectionno=soup.find_all('section')
d=['introduction','theory','objective','experiment','manual','quizzes','further_readings','procedure','hh','ll']
print len(sectionno)
sectionNumber=1
st=""
att = ''+'lab-article-heading'
tagger = soup.findAll('div', attrs={'id':att,'class':'heading'})
tag=str(tagger[0].txt)
