import sys
import time

from ast import literal_eval

filename = sys.argv[1]

out_filename = filename.replace(".txt", "_filtered.txt")

out_f_p = open(out_filename, "wt")

start_time = time.time()

with open(filename, "rt") as f_p:
    for line in f_p:
        try:
            data = literal_eval(line)

            date_download = data["date_download"]
            digest = data["digest"]

            raw_content = data["raw_content"]

            # Some filtering rules
            if "<" in raw_content:
                continue

            if ">" in raw_content:
                continue

            if "http:" in raw_content:
                continue

            if "https:" in raw_content:
                continue

            if "�" in raw_content:
                continue

            out_f_p.write(raw_content + "\n")

        except Exception as e:
            print(e)
            continue

print("Filtering for", filename, "took:", round(time.time() - start_time, 2), "seconds.")

out_f_p.close()
