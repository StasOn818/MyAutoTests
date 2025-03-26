import requests
TESTRAIL_URL = "https://silverhand818.testrail.io/"
API_KEY = "NY/N7DUaaGbbfkmjQXoe-N1fkh81.m2GnQorwkkiH"
PROJECT_ID = "4"

def update_test_result(test_case_id, status):
    url = f"{TESTRAIL_URL}/index.php?/api/v2/add_result_for_case/{PROJECT_ID}/{test_case_id}"
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "status_id": status,
        "comment": "Test executed using pytest and Python integration"
    }

    response = requests.post(url, json=data, auth=("stanislavkudriavtsev19@gmail.com", API_KEY), headers=headers)

    if response.status_code == 200:
        print(f"Test case {test_case_id} result updated successfully.")
    else:
        print(f"Failed to update TestRail for test case {test_case_id}. Status code: {response.status_code}")
