import requests
import datetime


def get_trending_repositories(top_size):
    r = requests.get(
        'https://api.github.com/search/repositories?q=created:>'+get_monday_date()+'&sort=stars')
    for item in r.json()['items'][:top_size]:
        print ('The repository "{}":\nLink:"{}"\nStars: {}\nOpen issues {}\n'.format(
            item['name'], item['html_url'], item['stargazers_count'], item['open_issues_count']))


def get_monday_date():
    return str((datetime.date.today() - datetime.timedelta(weeks=1)))


if __name__ == '__main__':
    get_monday_date()
    get_trending_repositories(20)
