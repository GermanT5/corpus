import sys
import time
import tarfile

from ast import literal_eval

filename = sys.argv[1]

out_filename = filename.replace(".tar.gz", ".txt")

out_f_p = open(out_filename, "wt")

start_time = time.time()

with tarfile.open(filename, "r:gz") as f_p:
    members = f_p.getmembers()

    print("Extracting:", members)

    assert len(members) == 1

    extracted_file = f_p.extractfile(members[0])

    file_content = extracted_file.read().decode('utf-8')

    file_content = file_content.replace("}{'url'", "}\n{'url'")

    for line in file_content.split("\n"):
        try:
            data = literal_eval(line)

            language_score = data["language_score"]

            if language_score > 0.98:
                out_f_p.write(line + "\n")
        except:
            continue

print("Extraction took:", round(time.time() - start_time, 2), "seconds.")

out_f_p.close()
