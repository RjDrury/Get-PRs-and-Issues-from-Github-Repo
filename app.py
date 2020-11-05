from github import Github
from constants import *
import csv
g = Github(access_token)
repo = g.get_repo("RjDrury/SOEN490")
issues = repo.get_issues(state="all")
print(issues)
with open("Issues.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["issue.name","issue.number", "issue.state", "issue.closed_at"])
    for issue in issues:
        wr.writerow([issue.title,issue.number, issue.state,issue.closed_at])

prs = repo.get_pulls(state="all")
with open("Pull-requests.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(["pr.title","PR Issue #" "pr.comments", "pr.review_comments", "pr.commits",  "pr.state", "pr.closed_at"])
    for pr in prs:
        wr.writerow([pr.title, pr.issue_url.split("/")[-1],pr.comments, pr.review_comments,pr.commits,  pr.state, pr.closed_at])