import requests
from bs4 import BeautifulSoup
import lxml

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; ry:102.0) Gecko/20100101 Firefox/102.0'}
url = "http//damoon-e.goeyp.kr/damoone/ad/fm/foodmenu/selectFoodMenuView.do?mi=3281"
res = requests.get(url, headers = header)
res.raise_for_status()

pip install requests
pip install lxml
pip install bs4