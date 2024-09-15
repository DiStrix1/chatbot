from django.shortcuts import render
from django.http import HttpResponse

# Simple "Hello, world!" view
def hello(request):
    return HttpResponse("Hello, world!")

# Company data dictionary (can be replaced with a database or CSV file)
company_data = {
    "Microsoft": {
        "2021": {"Revenue": "$168 billion", "NetIncome": "$30 billion", "Expenses": "$100 billion", "ProfitMargin": "40%", "StockPrice": "$289"},
        "2022": {"Revenue": "$198 billion", "NetIncome": "$60 billion", "Expenses": "$120 billion", "ProfitMargin": "45%", "StockPrice": "$310"},
        "2023": {"Revenue": "$211 billion", "NetIncome": "$70 billion", "Expenses": "$130 billion", "ProfitMargin": "48%", "StockPrice": "$335"},
    },
    "Apple": {
        "2021": {"Revenue": "$365 billion", "NetIncome": "$22 billion", "Expenses": "$250 billion", "ProfitMargin": "31%", "StockPrice": "$150"},
        "2022": {"Revenue": "$387 billion", "NetIncome": "$44 billion", "Expenses": "$270 billion", "ProfitMargin": "32%", "StockPrice": "$175"},
        "2023": {"Revenue": "$394 billion", "NetIncome": "$53 billion", "Expenses": "$280 billion", "ProfitMargin": "33%", "StockPrice": "$180"},
    },
    "Tesla": {
        "2021": {"Revenue": "$53 billion", "NetIncome": "$10 billion", "Expenses": "$30 billion", "ProfitMargin": "25%", "StockPrice": "$780"},
        "2022": {"Revenue": "$81 billion", "NetIncome": "$20 billion", "Expenses": "$50 billion", "ProfitMargin": "28%", "StockPrice": "$920"},
        "2023": {"Revenue": "$100 billion", "NetIncome": "$27 billion", "Expenses": "$60 billion", "ProfitMargin": "30%", "StockPrice": "$950"},
    }
}

# Function to get company info based on the query
def get_company_info(company, year, query_type):
    if company not in company_data:
        return "Invalid company selected."

    if year not in company_data[company]:
        return "Invalid year entered."

    data = company_data[company][year]

    # Query types and corresponding data
    if query_type == "revenue":
        return f"The total revenue for {company} in {year} is: {data['Revenue']}"
    elif query_type == "net income":
        return f"The net income for {company} in {year} is: {data['NetIncome']}"
    elif query_type == "expenses":
        return f"The total expenses for {company} in {year} are: {data['Expenses']}"
    elif query_type == "profit margin":
        return f"The profit margin for {company} in {year} is: {data['ProfitMargin']}"
    elif query_type == "stock price":
        return f"The stock price for {company} in {year} was: {data['StockPrice']}"
    else:
        return "Invalid query type."

# View to render the form (index page)
def index(request):
    return render(request, 'index.html')  # Ensure index.html exists in templates/playground/

# View to process the form submission
def get_info(request):
    if request.method == 'POST':
        company = request.POST.get('company').title()
        year = request.POST.get('year')
        query_type = request.POST.get('query_type').lower()

        # Get the result based on user input
        result = get_company_info(company, year, query_type)

        # Render the index page again with the result
        return render(request, 'index.html', {'result': result})

    # If the method is GET, render the form as usual
    return render(request, 'index.html')
