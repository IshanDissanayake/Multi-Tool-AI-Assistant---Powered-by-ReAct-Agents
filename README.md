# Multi-Tool-AI-Assistant---Powered-by-ReAct-Agents
## Overview
This repository contains the implementation of a **Multi-Tool AI Assistant** that leverages **ReAct (Reasoning and Action) agents** to interact with a variety of external tools for providing useful information. The assistant can perform web searches, retrieve weather information, and provide financial news updates, all through a simple conversational interface built with Streamlit.

## Features
- **Multi-Tool Integration**: The assistant utilizes a combination of tools for different functionalities:
    - **Web Search**: DuckDuckGo search tool for retrieving information from the web.
    - **Weather Information**: OpenWeatherMap API tool for getting weather data.
    - **Financial News**: Yahoo Finance tool to fetch the latest financial news.
      
- **ReAct Agents**: The assistant is powered by **ReAct agents** (Reasoning and Action agents) using Langchain's `AgentExecutor` framework. The ReAct agent processes user inputs and makes decisions based on predefined tools, executing actions in a step-by-step manner. It combines reasoning with action by:
    - First reasoning over the user's request to understand what needs to be done.
    - Then, executing the corresponding action by invoking one of the available tools.
      
- **Streamlit Interface**: The app is built with Streamlit, providing a user-friendly interface where users can interact with the assistant, get real-time responses, and view the assistant’s reasoning process.

## Tech Stack
- **LangChain**: For managing the agents and tools.
- **OpenAI API**: For the language model (LLM) powering the agent’s reasoning.
- **Streamlit**: For creating the interactive web app interface.
- **DuckDuckGo API**: For web search functionalities.
- **OpenWeatherMap API**: For fetching weather data.
- **Yahoo Finance API**: For retrieving financial news.

## Installation
To run the Multi-Tool AI Assistant locally, follow these steps:

1. ### Clone the repository <br>
`git clone https://github.com/IshanDissanayake/Multi-Tool-AI-Assistant---Powered-by-ReAct-Agents.git` <br>
`cd multi-tool-ai-assistant`

2. ### Install dependencies
Ensure you have Python 3.8+ installed, then install the required dependencies by running: <br>
`pip install -r requirements.txt`

3. ### Set up environment variables
You will need to configure your OpenAI API key and OpenWeatherMap API key as environment variables. Create a .env file in the root directory and add the following: <br>
`OPENAI_API_KEY=your-openai-api-key` <br>
`OPENWEATHERMAP_API_KEY=your-openweathermap-api-key`

4. ### Run the Streamlit app
Now, you can run the app using the following command: <br>
`streamlit run app.py`

This will start the Streamlit application, and you can access it in your browser.

## How It Works
1. Agent Initialization
The assistant is initialized using Langchain’s **AgentExecutor** class, which is responsible for managing the ReAct agent. The agent makes decisions based on the tools available to it, which include: 
    - **DuckDuckGoSearchRun**: For performing web searches.
    - **OpenWeatherMap API**: For retrieving current weather information.
    - **YahooFinanceNewsTool**: For getting the latest financial news.
2. ReAct (Reasoning and Action) Agent
The core of the assistant is powered by a **ReAct agent**, which performs the following actions:
    - **Reasoning**: The agent first analyzes the user's input to determine the best course of action, whether it needs to perform a web search, fetch weather data or retrieve financial news.
    - **Action**: After reasoning, the agent selects the appropriate tool(s) and invokes it to provide the necessary information.

3. Streamlit Interface
Users can interact with the assistant through a simple chat interface built with Streamlit. The assistant uses chat history to provide context for ongoing conversations. Users can ask questions, and the assistant will display its reasoning process and the resulting actions.

4. Multi-Step Execution
The assistant can handle complex queries by chaining multiple tools and reasoning steps together. This ensures that even complicated tasks, such as gathering weather information and financial news in a single query, are handled efficiently.

## License
This project is licensed under the `MIT License` - see the LICENSE file for details.
   
  







