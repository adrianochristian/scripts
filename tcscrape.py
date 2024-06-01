import cloudscraper
import pandas as pd
from time import gmtime, strftime
import env

crttime = strftime("%m/%d %H:%M", gmtime())

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

def resume(under, over):
    print(f"Date: {crttime}")
    print()
    print(f"Under 70%: {len(under)}")
    for i in range(len(under)):
        print(
            f'''
Match: {under['Home'].values[0]} vs {under['Away'].values[0]}
Corner Line: {under['Corner Line'].values[0]}
Avg. Corner: {under['Avg. Corner'].values[0]}
Tip: {under['Tips'].values[0]}
Stake: 1u
            ''')
    print()
    print(f"Over 70%: {len(over)}")
    for i in range(len(over)):
        print(
            f'''
Match: {over['Home'].values[0]} vs {over['Away'].values[0]}
Corner Line: {over['Corner Line'].values[0]}
Avg. Corner: {over['Avg. Corner'].values[0]}
Tip: {over['Tips'].values[0]}
Stake: 1u
            ''')

def resume_all(df):
    print(f"Date: {crttime}")
    print()
    print(f"Over 70% or Under 70%: {len(df)}")
    for i in range(len(df)):
        print(f"{df['Home'].values[i]} vs {df['Away'].values[i]}")

def main():
    response = get_page(env.url)
    df = set_df(response.content)
    df = hydrate(df)
    resume(get_under(df), get_over(df))

main()