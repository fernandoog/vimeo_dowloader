#pip install git+https://github.com/yashrathi-git/vimeo_downloader
import sys
from vimeo_downloader import Vimeo
print(f'Runnig {sys.argv}')
if len(sys.argv) < 2:
    raise ValueError('Please provide url. example https://vimeo.com/440801455')
url = sys.argv[1]

cookies = """h=943fe8f867""".strip()

try:
    v = Vimeo(
    url,
    cookies=cookies
    )
    best_stream = v.best_stream
    mp4_url = best_stream.direct_url

    title = best_stream.title

    ## Download
    best_stream.download()
    print(f'OK {best_stream.title}')
except Exception as e:
    print(e)
    print(f'ERROR {url}')

