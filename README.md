### Необходимо установить
```shell
python.exe -m pip install --upgrade pip
pip install streamlit
pip install python-dotenv
```

**Run streamlit**
```shell
streamlit run app.py
```

---
**примеры запроса**
```shell
http://srv-dev.bant.pro:8080/wc/btc?from=1675209600&to=1698796800&countback=10&resolution=120&cogort=1&label=nolabel&success=any
http://srv-dev.bant.pro:8080/wc/usd?from=1675209600&to=1698796800&countback=10&resolution=120&cogort=1&label=nolabel&success=any
http://srv-dev.bant.pro:8080/wc/profit?from=1675209600&to=1698796800&countback=10&resolution=120&cogort=1&label=nolabel&success=any
http://srv-dev.bant.pro:8080/wc/countwallets?from=1675209600&to=1698796800&countback=10&resolution=120&cogort=1&label=nolabel&success=any
http://srv-dev.bant.pro:8080/wc/accumulatedprofit?from=1675209600&to=1698796800&countback=10&resolution=120&cogort=1&label=nolabel&success=any
```

**Endpoints:**

| Name               | Endpoint              |
|--------------------|-----------------------|
| btc balance        | /wc/btc               |
| usd balance        | /wc/usd               |
| profit             | /wc/profit            |
| cummulative profit | /wc/accumulatedprofit |
| count of wallets   | /wc/countwallets      |
