
import requests

data = {
            "Emp_Id": 1008,
            "Name": "Nand K                                   ",
            "Technology": "GCP                                     ",
            "Gender": "male                                  "
        }

url = "http://34.170.55.94/create"

x = requests.post(url, json = data)
print(x.text)