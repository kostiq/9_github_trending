import requests
import datetime


def get_trending_repositories(top_size):
    last_week_date = str(datetime.date.today() - datetime.timedelta(weeks=1))
    payload = {'q': 'created:>'+last_week_date, 'sort': 'stars'}
    r = requests.get(
        'https://api.github.com/search/repositories', params=payload)
    return r.json()['items'][:top_size]


def pprint_repo_list(repositories):
    for repo in repositories:
        print ('''The repository {name!r}:
            Link:{html_url!r}
            Stars: {stargazers_count}
            Open issues: {open_issues_count}'''
               .format(**repo))


if __name__ == '__main__':
    pprint_repo_list(get_trending_repositories(20))
