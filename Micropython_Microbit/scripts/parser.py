import re
import os, glob
from collections import defaultdict
import requests

paths = glob.glob('**/*.md',recursive=True)
base_url = "https://github.com/PierreLaunay/SNT-I2D-SIN/blob/master/"
#print(path)
links = re.compile(r"\[.*?\]\((.*?)\)")
intern = re.compile(r"#\S*")
urls = re.compile(r"http")
requested_links = defaultdict(list)
for path in paths:
    try:
        file = open(path).read()
    except:
        print(path,"unable to open")
    finally:
        results=links.findall(file)
        for result in results:
            if intern.match(result):
                requested_links[path].append(base_url+path+result)
            elif urls.search(result):
                requested_links[path].append(result)
            else:
                requested_links[path].append(base_url+os.path.join(os.path.dirname(path),result))

logging = open("Micropython_Microbit/scripts/errors.log","w")
for a,b in requested_links.items():
    for c in b:
        try:
            webpage = requests.get(c)
        except requests.exceptions.SSLError:
            print(f"Security Error for {c} in {a}\n")
            try:
                webpage = requests.get(c, verify=False)
            except Exception as e:
                logging.write(f"Website not working correctly, see {e} for {c} in {a}\n")
        except requests.exceptions.InvalidURL:
            logging.write(f"Invalid URL Error for {c} in {a}\n")
        finally:
            if 200 <= webpage.status_code <= 299:
                print("Bravo !")
            else:
                logging.write(f"Faut revoir sa copie : {c} in {a}\n")
logging.close()
