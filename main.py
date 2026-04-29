from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
import os
from openai.types.responses import ResponseTextDeltaEvent
import sendgrid
from sendgrid.helpers.mail import Mail,Email,To,Content
import asyncio

load_dotenv(override=True)

instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

instructions3 = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."


sales_agent1= Agent(name="Sales agent", instructions=instructions1, model="gpt-4o-mini")
sales_agent2=Agent(name="Engaging Sales agent", instructions=instructions2, model="gpt-4o-mini")
sales_agent3=Agent(name="Busy Sales agent", instructions=instructions3, model="gpt-4o-mini")

#async def main():
#    response = Runner.run_streamed(sales_agent1, input="Generate a cold email to a potential customer who is a CTO of a mid-sized tech company. The email should highlight the benefits of using ComplAI for SOC2 compliance and audit preparation.")    
#    async for event in response.stream_events():
#        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#            print(event.data.delta,end="",flush=True)

#asyncio.run(main())



async def generateEmail():
    result = await  asyncio.gather(
    Runner.run(sales_agent1, input="Generate a cold email to a potential customer who is a CTO of a mid-sized tech company. The email should highlight the benefits of using ComplAI for SOC2 compliance and audit preparation."),
    Runner.run(sales_agent2, input="Generate a cold email to a potential customer who is a CTO of a mid-sized tech company. The email should highlight the benefits of using ComplAI for SOC2 compliance and audit preparation."),
    Runner.run(sales_agent3, input="Generate a cold email to a potential customer who is a CTO of a mid-sized tech company. The email should highlight the benefits of using ComplAI for SOC2 compliance and audit preparation.")
    )

    print(*[res.final_output for res in result], sep="\n")


asyncio.run(generateEmail())