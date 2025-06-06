from flask import Flask, render_template, request, jsonify
import tushare as ts
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 初始化 tushare
ts.set_token(os.getenv('TUSHARE_TOKEN'))
pro = ts.pro_api()

def get_stock_list():
    """获取股票列表"""
    data = pro.stock_basic(exchange='', list_status='L')
    return data[['ts_code', 'name']].values.tolist()

@app.route('/')
def index():
    """主页路由"""
    stocks = get_stock_list()
    return render_template('index.html', stocks=stocks)

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    """获取股票数据的API端点"""
    data = request.json
    ts_code = data.get('stock_code')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    indicator = data.get('indicator')

    # 获取日线数据
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    df = df.sort_values('trade_date')

    # 创建图表
    trace = go.Scatter(
        x=df['trade_date'],
        y=df[indicator],
        mode='lines',
        name=indicator
    )

    layout = go.Layout(
        title=f'{ts_code} - {indicator}',
        xaxis=dict(title='日期'),
        yaxis=dict(title=indicator)
    )

    fig = go.Figure(data=[trace], layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify({
        'graph': graphJSON,
        'data': df.to_dict('records')
    })

if __name__ == '__main__':
    app.run(debug=True) 