import requests
from os.path import exists


# HEADER = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "accept-encoding": 'gzip, deflate, br',
#     "accept-language": 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     'if-modified-since': 'Thu, 02 Jan 2020 20:10:29 GMT',
#     'if-none-match': "e767-59b2dc8e65f07",
#     "sec-fetch-dest": 'document',
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": 'none',
#     'sec-fetch-user': "?1",
#     'upgrade-insecure-requests': "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"
# }


def get_image_name(img_link: str):
    return img_link[img_link.rfind("/")+1:img_link.find("?")]


def download_image(img_link: str):
    print('Downloading', img_link, '...')
    filepath = f'../images/{get_image_name(img_link)}'
    if not exists(filepath):
        resolved = False
        trials = 0
        while not resolved and trials < 10:
            try:
                image_content = requests.get(img_link).content
                resolved = True
                with open(f'../images/{filepath}', 'wb') as f:
                    f.write(image_content)
                f.close()
            except Exception as e:
                print(e, 'Retrying')
                trials += 1
    else: print(filepath, 'Already exists')


with open('img_links.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        print(line)
        try:
            download_image(line)
        except Exception as e:
            print(e, line)
            pass
        print('Finished', get_image_name(line))

