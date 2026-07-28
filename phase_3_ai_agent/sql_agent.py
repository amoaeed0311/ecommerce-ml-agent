import os
from dotenv import load_dotenv
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq

# 1. Load Environment Variables from root .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

if not GROQ_API_KEY or not MYSQL_PASSWORD:
    raise ValueError(
        "Please ensure GROQ_API_KEY and MYSQL_PASSWORD are set in your root .env file!"
    )

# 2. Connect to MySQL Database via LangChain
DB_USER = "root"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"

db_uri = f"mysql+mysqlconnector://{DB_USER}:{MYSQL_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db = SQLDatabase.from_uri(db_uri)

print("✅ Connected to Database!")
print(f"📊 Tables available: {db.get_usable_table_names()}")

# 3. Initialize Groq LLM (Llama 3.3)
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=GROQ_API_KEY,
)

# 4. Create SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="zero-shot-react-description",
    verbose=True,  # Set to True to see the SQL generation steps in real time!
)

# 5. Interactive Question Loop
print("\n" + "=" * 55)
print("🤖 AI SQL DATA ANALYST AGENT READY")
print("=" * 55)
print("Type 'exit' or 'quit' anytime to stop the session.\n")

while True:
    user_query = input("\n💬 Ask a question about your e-commerce data: ")

    # Check for exit commands
    if user_query.strip().lower() in ["exit", "quit"]:
        print("\nClosing session. Great job on your project!")
        break

    # Skip empty inputs
    if not user_query.strip():
        continue

    try:
        # Run agent query using modern .invoke() syntax
        response = agent_executor.invoke({"input": user_query})

        print("\n📢 AGENT RESPONSE:")
        print(response["output"])
        print("-" * 55)

    except Exception as e:
        print(f"\n❌ Error executing agent query: {e}")