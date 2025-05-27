import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph, SearchGraph, SpeechGraph

load_dotenv()

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "openai/gpt-4o-mini",
      "temperature": 0.3,
   },
   "tts_model": {
      "api_key": openai_key,
      "voice":"nova",
   },
   "verbose": True,
   "headless": False,
}

# Create the SmartScraperGraph instance and run it

speech_graph = SpeechGraph(
   prompt="Make a detailed audio summary of the projects.",
   source="https://perinim.github.io/projects/",
   config=graph_config
)

result = speech_graph.run()
print(result)
