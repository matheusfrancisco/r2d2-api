import requests


def test_recommendations(user_id, answers):
    url_rec = f"http://127.0.0.1:8000/recommendations/{user_id}"
    r = requests.post(url=url_rec, json=answers)
    print(r.content)

if __name__ == "__main__":
    answers_ = {
        "how_much": 0,
        "like": 0,
        "number_of_ppl": 0,
    }
    test_recommendations(123, answers_)