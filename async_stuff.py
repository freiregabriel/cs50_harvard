import asyncio
import requests
import json
from bs4 import BeautifulSoup
from typing import Optional
import time
from concurrent.futures import ThreadPoolExecutor
import numba

def get_followers(profile: str, session) -> Optional[float]:
    """
    get instagram followers by passing your Instagram URL 
    Usage get_followers('https://www.instagram.com/gabrielfreiredev/')
    """
    url = f'https://www.instagram.com/{profile}'
    r = session.get(url)
    if r.ok:
        instagram = BeautifulSoup(r.text, features="lxml")
        scripts = instagram.select('script[type="text/javascript"]')
        json_s = scripts[3]
        json_s = json_s.text
        json_s = json_s[len('window._sharedData = '):-1]
        json_s = json.loads(json_s)
        entry_data = json_s['entry_data']
        profile_page = entry_data['ProfilePage'][0]
        graph_ql = profile_page['graphql']
        user = graph_ql['user']
        user['edge_owner_to_timeline_media'] = None
        with open(f'user_information_{profile}.json', 'w') as f:
            f.write(json.dumps(user, indent=4, sort_keys=True))
        follow_count = user['edge_followed_by']
        final: float = float(follow_count['count'])
        print(f'Finished for {profile} - Followers {final}')
        # await asyncio.sleep(0.01)
        return final
    return 0

async def get_followers_threading():
    profiles = ['gabrielfreiredev', 'freire.tatyana', 'sarahknight17', 'caabramacho', 'caabradapexte']
    res = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(executor, get_followers, *(profile, session)) for profile in profiles
                # get_followers(*(profile,), session) for profile in profiles
            ]
            for response in await asyncio.gather(*tasks):
                res.append(response)
    return res

async def get_followers_async():
    profiles = ['gabrielfreiredev', 'freire.tatyana', 'sarahknight17', 'caabramacho', 'caabradapexte']
    with requests.Session() as session:
        tasks = [
            get_followers(*(profile, session)) for profile in profiles
        ]
        print(tasks)
        await asyncio.gather(*tasks)
# async_tasks = asyncio.gather(*[get_followers('gabrielfreiredev'), get_followers('freire.tatyana')
#                                 ,get_followers('sarahknight17'),get_followers('caabramacho'), get_followers('caabradapexte')]) # Just like Promise.all([])
def main():
    start = time.time()
    loop = asyncio.get_event_loop()
    # future = asyncio.ensure_future(get_followers_async())
    future = asyncio.ensure_future(get_followers_threading())
    data = loop.run_until_complete(future) # will run all the async tasks in parallel
    # data = loop.run_until_complete(future)
    end = time.time()
    elapsed = end - start
    print(f"Took {elapsed} ms")
    print(data)
    loop.close()

main()