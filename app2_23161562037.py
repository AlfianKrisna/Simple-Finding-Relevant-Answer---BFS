from collections import deque

def find_relevant_answer(faq_graph, query):
    queue = deque([query])
    visited = set()
    
    while queue:
        node = queue.popleft()
        
        if node in faq_graph.get("answers", {}):
            return faq_graph["answers"][node]
        
        if node not in visited:
            visited.add(node)
            queue.extend(faq_graph.get(node, []))
    
    return "No relevant answer found."

# Contoh penggunaan
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

query = "What is AI?"
print("Relevant Answer:", find_relevant_answer(faq_graph, query))
