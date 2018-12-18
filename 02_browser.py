import webbrowser

q_list = ["bts", "아이유", "블랙핑크", "송민호"]

url = "https://www.google.com/search?q="

for q in q_list:
    webbrowser.open(url + q)
#webbrowser.open_new(url)