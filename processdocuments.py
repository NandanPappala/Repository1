from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Initialize smart text splitter") 
# 1. Initialize the smart text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # Max characters per chunk
    chunk_overlap=200,     # Overlap between adjacent chunks
    length_function=len,   # How to measure chunk length
    is_separator_regex=False,
)

