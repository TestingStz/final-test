import os
import requests
import json
import re

def extract_section(content, section_heading):
    pattern = rf"{section_heading}\s*\n*([^#]+)"
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ''

def main():
    title = os.getenv('INPUT_TITLE')
    body = os.getenv('INPUT_BODY')
    origin_repo_url = os.getenv('GITHUB_SERVER_URL') + os.getenv('GITHUB_REPOSITORY')

    bug_description = extract_section(body, "### 1. **Bug/Vulnerability Description**")
    hardware_software_specs = extract_section(body, "### 2. **Hardware and Software Specifications**")
    steps_to_reproduce = extract_section(body, "### 3. **Steps to Reproduce**")
    impact_analysis = extract_section(body, "### 4. **Impact Analysis**")
    code_fix_submission = extract_section(body, "### 5. **Code Fix Submission**")
    choose_the_right_label = extract_section(body, "### 6. **Choose the Right Label**")
    additional_context = extract_section(body, "### 7. **Additional Context**")

    body_with_link = f"**Bug/Vulnerability Description:**\n{bug_description}\n\n**Hardware and Software Specifications:**\n{hardware_software_specs}\n\n**Steps to Reproduce:**\n{steps_to_reproduce}\n\n**Impact Analysis:**\n{impact_analysis}\n\n**Code Fix Submission:**\n{code_fix_submission}\n\n**Choose the Right Label:**\n{choose_the_right_label}\n\n**Additional Context:**\n{additional_context}\n\nComments are not being updated\nOriginal Issue can be found [here]({origin_repo_url})"

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

    response = requests.post(create_issue_url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Issue successfully created in Bug_Bounty_v1 repository.")
    else:
        print(f"Failed to create issue. Status code: {response.status_code}, Error message: {response.text}")

if __name__ == "__main__":
    main()
