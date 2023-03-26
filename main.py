from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def chat():
# Web scrappying to get image link
    url = "https://ibighit.com/ "

    responds = requests.get(url)
    soup = BeautifulSoup(responds.content, "html.parser")
    images = soup.find_all(class_="responsiveImg")
    titles = soup.find_all(class_="contents-title")

    img_list = []
    title_list = []

    for t in titles:
        title_list.append(t.getText())
    print(title_list)

    for img in images:
        image_src = img["data-media-web"]
        img_str = str(image_src)
        # print(img_str)

# splitting to reconstruct the image link gotten
        x = img_str.split(".")
        try:
            x.remove(x[0])
            img_src = f"https://ibighit.com{x[1]}.{x[2]}"
            img_list.append(img_src)

        except IndexError:
            img_src = f"https://ibighit.com{x[0]}.{x[1]}"
            img_list.append(img_src)
            # print(img_src)

    return render_template("index.html", pic1=img_list[0],pic2=img_list[1], pic3=img_list[2],
                           pic4=img_list[3], pic5=img_list[4], title1=title_list[0], title2=title_list[1],
                           title3=title_list[2], title4=title_list[3], title5=title_list[4])



if __name__ == "__main__":
    app.run(debug=True)
