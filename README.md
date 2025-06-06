# Tushare 网页指标查询

这是一个基于 Flask 和 Tushare 开发的股票指标分析网站，支持查询 A 股上市公司的各项交易指标。

## 功能特点

- 支持查询所有 A 股上市公司的股票数据
- 可自由选择查询时间范围
- 支持多种交易指标的查询：
  - 开盘价
  - 最高价
  - 最低价
  - 收盘价
  - 成交量
  - 成交额
- 数据可视化展示：
  - 交互式图表展示（基于 Plotly）
  - 详细数据表格展示

## 环境要求

- Python 3.7+
- pip 包管理器

## 安装步骤

1. 克隆或下载本项目到本地

2. 创建并激活虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
# 先安装 numpy（必须）
pip install numpy==1.21.2

# 然后安装其他依赖
pip install -r requirements.txt
```

4. 配置 Tushare Token：
   - 在 [Tushare官网](https://tushare.pro/) 注册并获取 API Token
   - 在项目根目录创建 `.env` 文件
   - 在 `.env` 文件中添加：
     ```
     TUSHARE_TOKEN=你的token
     ```

## 运行应用

1. 在项目根目录下运行：
```bash
python app.py
```

2. 打开浏览器访问：`http://localhost:5000`

## 技术栈

- 后端：Flask
- 数据源：Tushare
- 前端框架：Bootstrap
- 图表库：Plotly
- 数据处理：Pandas, NumPy

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。 