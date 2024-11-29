from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

model= ChatOpenAI(model="gpt-4")
memory = SqliteSaver.from_conn_string(":memory:")

search= TavilySearchResults(max_results=2)

tools=[search]

agent_executor = create_react_agent(model, tools,checkpointer=memory)

config = {"configurable": {"thread_id":""
                                       "123"}}

if __name__ == "__main__":
    while True:
        user_input = input(">")
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}, config
        ):
            print(chunk)
            print("----")
