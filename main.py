from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Crimson Innovative Technologies is a leading provider of innovative solutions that help clients achieve their business goals. Our high-tech services support co-innovation and thought leadership, leveraging continuous research and development in areas such as AI/ML, Embedded & IoT, Robotics, Edge AI, Application services, data analytics, cloud computing, Test Automation, and storage technologies. Our services empower clients to capitalize on emerging technologies, reduce development time and costs, and seize market opportunities, allowing them to introduce the best products for their customers.
    """
    summary_template = """
    given the information {information} about a company I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=[information],template=summary_template)
    llm = ChatOllama(temperature=0,model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)
    


if __name__ == "__main__":
    main()
