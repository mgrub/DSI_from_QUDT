import os

import requests

onto_sources = {
    "qudt.ttl":"http://qudt.org/2.1/schema/qudt",
    "datatype.ttl":"http://qudt.org/2.1/schema/datatype",
    "unit.ttl":"http://qudt.org/2.1/vocab/unit",
    "quantitykind.ttl":"http://qudt.org/2.1/vocab/quantitykind",
    "dimensionvector.ttl":"http://qudt.org/2.1/vocab/dimensionvector",
    "constant.ttl":"http://qudt.org/2.1/vocab/constant",
    "sou.ttl":"http://qudt.org/2.1/vocab/sou",
    "soqk.ttl":"http://qudt.org/2.1/vocab/soqk",
}

cache_dir_path = "onto_cache"
if not os.path.exists(cache_dir_path):
    os.mkdir(cache_dir_path)

for filename, url in onto_sources.items():

    cache_file_path = os.path.join(cache_dir_path, filename)

    if os.path.exists(cache_file_path):
        print(f"{filename}: using cached version.")

    else:
        res = requests.get(url)

        if res.status_code == 200:
            f = open(cache_file_path, "wb")
            f.write(res.content)
            f.close()
            print(f"{filename}: downloaded and saved.")

        else:
            print(f"{filename}: issue during download.")
