# stock_graph/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def stock_detail(request, stock_name="AAPL"):
    api_key = 'ON1JESXTV3EDXH8I'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_name}&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    try:
        time_series = data['Time Series (Daily)']
    except KeyError:
        # If 'Time Series (Daily)' key is not present, print the response for debugging
        print("API response does not contain 'Time Series (Daily)' key:")
        print(data)
        return JsonResponse({'error': 'Invalid API response'})

    stock_data = []

    for date, values in time_series.items():
        stock_data.append({
            'date': date,
            'open_price': float(values['1. open']),
            'high_price': float(values['2. high']),
            'low_price': float(values['3. low']),
            'close_price': float(values['4. close']),
        })

    return render(request, 'stock_graph/stock_detail.html', {'stock_data': json.dumps(stock_data)})
