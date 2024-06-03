import cloudscraper
import pandas as pd
import telegram
from time import gmtime, strftime
import env

crttime = strftime("%d/%m", gmtime())

def get_page(url):
    try:
        scraper = cloudscraper.create_scraper()
        return scraper.get(url)
    except Exception as e:
        print(f"An error occurred while trying to get the page: {e}")
        return None

def set_df(response):
    dataframe = pd.read_html(response)[0]
    return dataframe

def hydrate(df):
    df = df.dropna(axis=1, how='all')
    df = df.drop(columns=['Unnamed: 4', 'Unnamed: 12'])
    df = df.rename(columns={'Over% Under%' : 'Over%', 'Over% Under%.1' : 'Under%'})
    return df

def get_under(df):
    return df.where(df['Under%'] >= 70).dropna(axis=0, how='all')

def get_over(df):
    return df.where(df['Over%'] >= 70).dropna()

def get_all(df):
    #TODO: Analyze working with query for experimental purposes in the future
    return df.query('`Over%` >= 70 or `Under%` >= 70')

def save_to_txt(game):
    with open('list.txt', 'a') as f:
        f.write(game)
        f.write('\n')
        f.close()

def send_message(message):
    if message not in open('list.txt').read():
        telegram.send_message(message)
        save_to_txt(message)

def resume(under, over):
    for i in range(len(under)):
        send_message(
            f'''
            Date: {under['Time'].values[i]}
            Match: {under['Home'].values[i]} vs {under['Away'].values[i]}
            Corner Line: {under['Corner Line'].values[i]}
            Avg. Corner: {under['Avg. Corner'].values[i]}
            Tip: {under['Tips'].values[i]}
            Stake: 1u
            ''')
    for i in range(len(over)):
        send_message(
            f'''
            Date: {over['Time'].values[i]}
            Match: {over['Home'].values[i]} vs {over['Away'].values[i]}
            Corner Line: {over['Corner Line'].values[i]}
            Avg. Corner: {over['Avg. Corner'].values[i]}
            Tip: {over['Tips'].values[i]}
            Stake: 1u
            ''')

def resume_all(df):
    print(f"Date: {crttime}")
    print()
    print(f"Over 70% or Under 70%: {len(df)}")
    for i in range(len(df)):
        print(f"{df['Home'].values[i]} vs {df['Away'].values[i]}")

def main():
    response = get_page(env.URL)
    df = set_df(response.content)
    df = hydrate(df)
    resume(get_under(df), get_over(df))

main()