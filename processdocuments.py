from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Initialize smart text splitter") 
# 1. Initialize the smart text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # Max characters per chunk
    chunk_overlap=200,     # Overlap between adjacent chunks
    length_function=len,   # How to measure chunk length
    is_separator_regex=False,
)



document_content = """You will also learn about the different levels of Git configuration, specifically global and local settings, and how to list them. Finally, we will briefly touch upon how to handle cases where the user name is not yet configured. This lab will equip you with the knowledge to ensure your Git setup correctly identifies your contributions.
Use git config user.name to Check
In this step, we will learn how to check your Git configuration, specifically your user name. Git uses this information to identify who made each commit."""

chunks = splitter.split_text(document_content)

# 3. Output results
print(f"Created {len(chunks)} chunks.")
for i, chunk in enumerate(chunks[:3]):
    print(f"--- Chunk {i+1} ---")
    print(chunk[:200]) # Print first 150 characters