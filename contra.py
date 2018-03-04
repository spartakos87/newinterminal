import feedparser as rss
from greek_sites_crawler import greek_sites_crawler as gr
from pprint import pprint as pp

class Contra:
	def __init__(self):
		rss_link = "http://www.contra.gr/?widget=rssfeed&view=feed&contentId=1169269"
		self.data = rss.parse(rss_link)["entries"]
		self.titles = [i["title"] for i in self.data]
		self.links = [i["link"] for i in self.data]

	def PrintTitles(self):
		for k,i in enumerate(self.titles):
			print(str(k+1)+"."+i+"\n")
		self.Choose()

	def Choose(self):
		index = input("\nGive the number of title you want to read the article:\n")
		self.link = self.links[int(index)-1]
		self.PrintArticle()

	def PrintArticle(self):
		article = gr(self.link)
		pp(article.get_data())
		
	
		
		
