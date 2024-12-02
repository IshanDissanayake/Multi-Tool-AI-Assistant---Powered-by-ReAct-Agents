import os
import logging
import streamlit as st
from typing import List, Dict, Any
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain.agents import load_tools, create_react_agent, AgentExecutor
from langchain.tools import BaseTool
from langchain import hub

class MultiToolAgent:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        load_dotenv()
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
        os.environ["OPENWEATHERMAP_API_KEY"] = os.getenv('OPENWEATHERMAP_API_KEY')

        self.llm = ChatOpenAI(model = 'gpt-3.5-turbo', temperature = 0)
        self.tools = self._initialize_tools()
        self.agent = self._create_agent()

    
    def _initialize_tools(self) -> List[BaseTool]:
        try:
            #web search tool
            web_search_tool = DuckDuckGoSearchRun()

            #yahoo finance news tool
            fin_news_tool = YahooFinanceNewsTool()

            #weather tool
            weather_api_tool = load_tools(["openweathermap-api"], self.llm)[0]

            return [web_search_tool, weather_api_tool, fin_news_tool]
            
        
        except Exception as e:
            self.logger.error(f"Error loading tools: {e}")
            return []

    def _create_agent(self) -> AgentExecutor:
        try:
            #define prompt template
            prompt = hub.pull("hwchase17/react")

            #create agent
            agent = create_react_agent(tools=self.tools, llm=self.llm, prompt=prompt)

            #initialize agent executor
            return AgentExecutor(agent=agent, 
                        tools=self.tools, 
                        verbose=True, 
                        handle_parsing_errors=True, 
                        max_iterations=10, 
                        early_stopping_method='force'
                        )
        
        except Exception as e:
            self.logger.error(f"Error creating agent: {e}")
            return None
        
    def execute_query(self, query:str) -> Dict[str, Any]:
        try:
            if not self.agent:
                raise ValueError("Agent not initialized properly")

            response = self.agent.invoke({"input": query})
            return response

        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            return {"output": "Sorry, I encountered an error processing your request."}

    
def main():
    # Streamlit app configuration
    st.set_page_config(page_title="Multi-Tool AI Assistant", page_icon="🤖")
    
    # Title and description
    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Title and description
    st.markdown('<h1 class="centered-text">🤖 Multi-Tool AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="centered-text">An intelligent assistant that can help with web searches, weather information, and financial news.</p>', unsafe_allow_html=True)
    
    # Initialize the agent
    if 'agent' not in st.session_state:
        st.session_state.agent = MultiToolAgent()
    
    # Chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.execute_query(prompt)
                assistant_response = response.get('output', 'No response generated.')
                st.markdown(assistant_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()
