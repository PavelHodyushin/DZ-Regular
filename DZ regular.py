import re


def extract_image_links(html_text):
    html_texts = []
    search = r'((http|https)(://).*?\..*?\/.*?\.(jpg|jpeg|png|gif))'
    searching_http = re.finditer(search, html_text)
    for matched in searching_http:
        html_texts.append(matched[0])
        #print(f"Следующие совпадение: {searching_http}")
    return html_texts

sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")


image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")