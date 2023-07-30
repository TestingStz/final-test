import os
import requests

def main():
    title = os.getenv('INPUT_TITLE')
    body = os.getenv('INPUT_BODY')
    origin_repo_url = os.getenv('GITHUB_SERVER_URL') + os.getenv('GITHUB_REPOSITORY')

    # Format the new issue body with both title and content from the template
    body_with_link = f"**Bug/Vulnerability Description:**\n{body}\n\nComments are not being updated\nOriginal Issue can be found [here]({origin_repo_url})"

    data = {
        "title": f"[External Issue] {title}",
        "body": body_with_link
    }

    main_repo_token = os.getenv('INPUT_MAIN_REPO_TOKEN')
    main_repo = os.getenv('INPUT_MAIN_REPO')
    create_issue_url = f"https://api.github.com/repos/{main_repo}/issues"

    headers = {
        "Authorization": f"token {main_repo_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.post(create_issue_url, headers=headers, json=data)

    if response.status_code == 201:
        print("Issue successfully created in Bug_Bounty_v1 repository.")
    else:
        print(f"Failed to create issue. Status code: {response.status_code}, Error message: {response.text}")

if __name__ == "__main__":
    main()
