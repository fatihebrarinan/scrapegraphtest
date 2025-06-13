import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "openai/gpt-4o-mini",
      "temperature": 0.3,
   },
   "verbose": True,
   "headless": False,
}


smart_scraper_graph = SmartScraperGraph(
    prompt="Extract the list of top movies from the page, including each movie's title, release year, rating, and the link to its detail page.",
    source="https://www.imdb.com/chart/top",
   config=graph_config
)

result = smart_scraper_graph.run()
print(result)
