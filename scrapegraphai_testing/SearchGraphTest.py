import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph

load_dotenv()

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "openai/gpt-4o-mini",
      "temperature": 0.3,
   },
   "library":"beautifulsoup4",
   "verbose": True,
   "headless": False,
}


search_graph = SearchGraph(
    prompt = "What is ChatGPT, how does it work, and in which fields is it used?",
   config=graph_config
)

result = search_graph.run()
print(result)
