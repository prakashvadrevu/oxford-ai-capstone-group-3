from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import CallbackManagerForChainRun
from typing import Any, Dict, Optional
import os

class CustomGraphCypherQAChain(GraphCypherQAChain):
    """Customized version of GraphCypherQAChain with overridden _call method."""

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        response = super()._call(inputs, run_manager)

        self.log(run_manager, "Db response\n" + str(response))

        context = f"""
        {response}

        Note: Do not include any explanations or apologies in your responses. Do not say I don't know the answer.
        Parse the query and the graph db response, and return a human readable response.
        """

        result = self.qa_chain(
            {"question": inputs['query'], "context": context}
        )
        return {'result': result[self.qa_chain.output_key]}

    def log(self, run_manager, text):
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        _run_manager.on_text(
            text, color="green", end="\n", verbose=self.verbose
        )

class CustomQAChain():

    def __init__(self):
        self.setup_keys()
        self.setup_graph()

    def setup_keys(self):
        # Replace these with appropriate keys
        os.environ["OPENAI_API_KEY"] = 'OXFORD_OPENAI_API_KEY'
        os.environ["NEO4J_URI"] = 'NEO4J_URI'
        os.environ["NEO4J_USERNAME"] = "neo4j"
        os.environ["NEO4J_PASSWORD"] = 'NEO4J_PASSWORD'

    def setup_graph(self):
        self.graph = Neo4jGraph(
            url=os.environ["NEO4J_URI"],
            username=os.environ["NEO4J_USERNAME"],
            password=os.environ["NEO4J_PASSWORD"]
        )

    # Support for 'history' is yet to be built.
    def run(self, question, history):
        hydrated_question = f"""
        ## Generate 
        {question}

        ## Instructions:
        The cypher query RETURN statement should contain all the relevant nodes and relationships in the result like store ID, country, categorgy, product and other.

        """
        chain = CustomGraphCypherQAChain.from_llm(
            ChatOpenAI(model="gpt-4o", temperature=0.5),
            graph=self.graph,
            verbose=True,
            return_direct=True
        )
        return chain.run(hydrated_question)