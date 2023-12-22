from django.shortcuts import render
from .models import StockData
import yfinance as yf
from datetime import datetime
from django.utils import timezone
import plotly.graph_objects as go
import pandas as pd

def stock_detail(request):
    symbol = 'RELIANCE.BO'  # Reliance stock symbol
    data = yf.download(symbol, start=timezone.now(), end=timezone.now(), progress=False)

    for index, row in data.iterrows():
        StockData.objects.create(symbol=symbol, date=index, price=row['Close'])

    stock_data = StockData.objects.filter(symbol=symbol)

    # Plotly candlestick chart
    candlestick_fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                     open=data['Open'],
                                                     high=data['High'],
                                                     low=data['Low'],
                                                     close=data['Close'],
                                                     increasing_line_color='green',
                                                     decreasing_line_color='red')])

    candlestick_fig.update_layout(
        title='Candlestick Chart for RELIANCE.BO',
        yaxis_title='Stock Price',
        xaxis_title='Date',
        shapes=[dict(
            x0='2020-12-09', x1='2023-12-31', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2016-12-09', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Increase Period Begins')],
        xaxis=dict(
            rangeslider=dict(
                visible=False
            )
        ),
        bargap=100,  # Adjust the gap between candlesticks (0.2 means 20% of the available space)
    )

    # Convert the Plotly chart to HTML
    candlestick_html = candlestick_fig.to_html(full_html=False)

    return render(request, 'stockapp/stock_detail.html', {'stock_data': stock_data, 'candlestick_html': candlestick_html})
