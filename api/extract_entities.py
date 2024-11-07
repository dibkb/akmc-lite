from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from api.graph import llm

prompt_template = """
Given the following description, identify and extract the specified entities.
If an entity's value is not present in the description, respond with "NaN".

Entities to extract:
- Operating_System
- Software_Component
- Version
- Impact
- Affected_Hardware
- Network_Requirements
- Affected_Protocols
- Authentication_Required
- Privileges_Required
- User_Interaction_Required
- Vendor

Description: {description}

Response format:
Operating_System: <value>
Software_Component: <value>
Version: <value>
Impact: <value>
Affected_Hardware: <value>
Network_Requirements: <value>
Affected_Protocols: <value>
Authentication_Required: <value>
Privileges_Required: <value>
User_Interaction_Required: <value>
Vendor: <value>
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["description"])
entity_extraction_chain = LLMChain(llm=llm, prompt=prompt)