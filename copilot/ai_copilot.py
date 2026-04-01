def ask(question):

    q = question.lower()

    if "vertex" in q:
        return "Vertex is a tax determination engine used to calculate taxes during transactions."

    if "middleware" in q:
        return "Middleware transfers transaction data between ERP systems and tax engines."

    if "tax reporting" in q:
        return "Tax reporting aggregates transaction tax data and generates regulatory reports."

    return "Ask me about tax systems."