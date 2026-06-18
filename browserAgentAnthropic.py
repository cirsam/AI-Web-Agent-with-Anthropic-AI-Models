import browser_use # import browser_use by first running pip install browser_use in your terminal and pip install playwright playwrite is used to control browser #action automation developed by Microsoft.
from browser_use import Agent
#pip install langchain_anthropic # run this first in the terminal to install langchain_anthropic. Playwright
from langchain_anthropic import ChatAnthropic #remove this line and use the browser_use import of ChatAnthropic instead of the langchain_anthropic import
from browser_use import Agent, ChatBrowserUse
#run this if you are having provider errors pip install --upgrade crewai langchain-anthropic browser-use after running pip install langchain-anthropic
from browser_use.llm.anthropic.chat import ChatAnthropic #import ChatAnthropic  from browser_use instead of langchain to avoid the error provider not set


import asyncio # this helps to create asynchronous methods
from dotenv import load_dotenv #you have to run pip install browser-use anthropic python-dotenv before this line


import os # this contains methods like os.environ used to create environmental variables.

load_dotenv() # this helps load the environmental variables
async def main():
 # Set your Anthropic API key
 os.environ["ANTHROPIC_API_KEY"]="put your anthropic API key here"

 
     # pay attention and make sure they are right, the ANTHROPIC_API_KEY and model name, Anthropic does not name its models with dots in them. If you use the wrong model name, you will get errors like 
    #Result failed 6/6 times: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error'
    
 llm = ChatAnthropic( model="claude-opus-4-8",timeout=None,max_retries=2,api_key=os.environ["ANTHROPIC_API_KEY"],)
 #llm = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")
 #llm = WrappedChatAnthropic(model="claude-3-5-sonnet-20240620")

 agent =  Agent(task="Go to Google,search for GHana and get the about content",llm=llm,)
    
 response= await agent.run()
 await asyncio.sleep(3)
 if __name__ == "__main__":
  print("Hello1")
 else:
  print("Hello2")
   
asyncio.run(main()) # don't use await here, it will result in an error
#always run this file in the terminal, I used PowerShell on a Windows machine 
# C:\path\to\your\python\file> python fileName.py follow the steps in this file from the top, copy and paste the content of this file, and save it in your fileName.py.then run it like this  in PowerShell C:\path\to\your\python\file> python fileName.py