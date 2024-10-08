import requests

parameters = {
    "amount" : 10,
    "type" : "boolean"
}
questions = requests.get("https://opentdb.com/api.php", params=parameters)
question_list = questions.json()
question_data = question_list["results"]