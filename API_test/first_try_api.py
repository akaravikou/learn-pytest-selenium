import requests
import uuid

from config.config import TestData


# response = requests.get(ENDPOINT)
# print(response)
#
# data = response.json()
# print(data)
#
# status_code = response.status_code
# print(status_code)


def test_endpoint_available():
    response = requests.get(TestData.ENDPOINT)
    assert response.status_code == 200, 'Resource is not available'


def test_create_task():
    payload = get_new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_update_task():
    payload = get_new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]


def test_list_tasks():
    number_of_tasks = 3
    payload = get_new_task_payload()
    for _ in range(number_of_tasks):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    user_id = payload["user_id"]
    list_tasks_response = get_list_tasks(user_id)
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    tasks = data["tasks"]
    assert len(tasks) == number_of_tasks


def test_delete_task():
    payload = get_new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


def create_task(payload):
    return requests.put(TestData.ENDPOINT + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(TestData.ENDPOINT + f"/get-task/{task_id}")


def get_new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }


def update_task(payload):
    return requests.put(TestData.ENDPOINT + "/update-task", json=payload)


def get_list_tasks(user_id):
    return requests.get(TestData.ENDPOINT + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(TestData.ENDPOINT + f"/delete-task/{task_id}")
