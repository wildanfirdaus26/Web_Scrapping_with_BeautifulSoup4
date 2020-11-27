from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

table = soup.find('table', attrs={'class':'table table-striped table-hover table-hover-solid-row table-simple history-data'})
tr = table.find_all('tr')
temp = [] #initiating a tuple

for i in range(1, len(tr)):
#insert the scrapping process here
    row = table.find_all('tr')[i]
    
    #get daily price (harga harian)
    daily_price = row.find_all('td')[2].text
    daily_price = daily_price.strip() #for removing the excess whitespace
    
    #get date (tanggal)
    date = row.find_all('td')[0].text
    date = date.strip() #for removing the excess whitespace
    
    temp.append((date,daily_price)) 

temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns=('date','daily_price'))

#insert data wrangling here
df['date'] = pd.to_datetime(df['date'])
df['daily_price'] = df['daily_price'].str.replace(',', '')
df['daily_price'] = df['daily_price'].str.replace('IDR', '')
df['daily_price'] = df['daily_price'].astype(float).round(2)

df['month'] = df['date'].dt.month_name()
df['month'] = df['month'].astype('category')
df = df[['date', 'month', 'daily_price']]

df = df.drop([0])
#end of data wranggling 

df_tab = pd.crosstab(
                index = df['month'],
                columns = 'daily_price',
                values= df['daily_price'],
                aggfunc= ('max','min','mean')
)

month_order = ["June", "July", "August", "September", "October", "November"]
df_tab.index = pd.CategoricalIndex(df_tab.index,\
                        categories=month_order,\
                        ordered=True)
df_tab = df_tab.sort_index()

df_tab.sort_index().plot(kind='bar')

@app.route("/")
def index(): 
	
	card_data = f'USD {df["daily_price"].mean().round(2)}'

	# generate plot
	ax = df_tab.plot(figsize = (20,9))
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
