from flask import Flask, render_template, request, redirect, flash
from scrap import scrapper

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
bot = scrapper()

scrap_result = "Nothing here yet"

@app.route('/', methods=['POST', 'GET'])
def home():
    global scrap_result
    # src, parser = scrape_site(URL)
    # return str(src)
    if request.method == 'POST':
        url = request.form['url']
        try:
            assert url != '', 'URL Must not be empty'
            flash('Scrapping...Please Wait...')
            scrap_result, _ = bot.scrape_site(url)
            flash('Success!Click [Show Results] to see result')
        except Exception as e:
            # return 'ERROR: Failed scrapping{}\n\t{}'.format(url, e)
            flash('ERROR,failed to scrap:{}'.format(url), 'error')
        return redirect('/')
    else:
        # tasks = TD.query.order_by(TD.date_created).all()
        return render_template('index.html')


@app.route('/scarp_result')
def show_result():
    return scrap_result


if __name__ == '__main__':
    URL = 'https://ryan47liao.github.io/Ryan-Portfolio/'
    app.run(debug=True)
