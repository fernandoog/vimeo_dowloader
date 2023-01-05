import sys
from vimeo_downloader import Vimeo

if len(sys.argv) != 2:
    raise ValueError('Please provide url.')
print(f'Url is {sys.argv[1]}')
url = sys.argv[1]

cookies = "".strip()

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
except Exception:
    print(f'ERROR {url}')

