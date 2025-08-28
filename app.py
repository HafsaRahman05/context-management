import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich

# 1. BANK ACCOUNT CONTEXT
class BankAccount(BaseModel):
    account_number: int | str
    customer_name: str
    account_balance: float
    account_type: str

bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Hafsa Rahman",
    account_balance=975500.50,
    account_type="savings"
)
@function_tool
def get_bank_info(wrapper: RunContextWrapper[BankAccount]):
    return f'The user info is {wrapper.context}'

bank_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get bank information",
    tools=[get_bank_info]
)

# 2. STUDENT PROFILE CONTEXT
class StudentProfile(BaseModel):
    student_id: int | str
    student_name: str
    current_semester: int
    total_courses: int

student = StudentProfile(
    student_id="STU-247",
    student_name="Hafsa Rahman",
    current_semester=4,
    total_courses=5
)
@function_tool
def get_student_info(wrapper: RunContextWrapper[StudentProfile]):
    return f'The user info is {wrapper.context}'

student_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get student information",
    tools=[get_student_info]
)

# 3. LIBRARY BOOK CONTEXT
class LibraryBook(BaseModel):
    book_id: int | str
    book_title: str
    auther_name: str
    is_available: bool

library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    auther_name="John Smith",
    is_available=True
)

@function_tool
def get_book_info(wrapper: RunContextWrapper[LibraryBook]):
    return f'The user info is {wrapper.context}'

Library_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get book information",
    tools=[get_book_info]
)

async def main():
    # Bank Agent Run
    result = await Runner.run(
        bank_agent, 
        # 'What is the account number', 
        'Please tell me my account details', 
        run_config=config,
        context = bank_account #Local context
        )
    rich.print(result.final_output)
    # Student Agent Run
    result = await Runner.run(
        student_agent, 
        # 'What is the user id', 
        'please tell me my student details', 
        run_config=config,
        context = student #Local context
        )
    rich.print(result.final_output)
    # Library Agent Run
    result = await Runner.run(
        Library_agent, 
        # 'What is the user id', 
        'please tell me my books details', 
        run_config=config,
        context = library_book #Local context
        )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())


