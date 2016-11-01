import requests
import datetime


def get_trending_repositories(top_size):
    r = requests.get(
        'https://api.github.com/search/repositories?q=created:>'+get_monday_date()+'&sort=stars')
    return r.json()['items'][:top_size]


def get_monday_date():
    return str((datetime.date.today() - datetime.timedelta(weeks=1)))


def pprint_repo_list(repositories):
    for repo in repositories:
        print ('The repository "{}":\nLink:"{}"\nStars: {}\nOpen issues {}\n'.format(
            repo['name'], repo['html_url'], repo['stargazers_count'], repo['open_issues_count']))


if __name__ == '__main__':
    pprint_repo_list(get_trending_repositories(20))
