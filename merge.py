import pandas as pd
import csv


BASE_FREQ = 1001.2939453125

mic_input_data = pd.read_csv('flatmicinput.txt', delimiter="\t", header=0, index_col="Hz").round(2).to_dict(orient='dict')

speaker_data = pd.read_csv('fullrespink.txt',delimiter="\t", header=0, index_col="Hz").round(2).to_dict(orient='dict')


mic_input_res = mic_input_data["dB"]
speaker_res = speaker_data["dB"]
base_db = mic_input_res[BASE_FREQ]

mic_input_offset = {}
for k, v in mic_input_res.items():
    mic_input_offset[k] = round((base_db - v), 2)

corrected_spkr_res = {}
for k, v in speaker_res.items():
    print(v)
    corrected_spkr_res[k] = round((v + mic_input_offset[k]), 2)

output_data = corrected_spkr_res.items()
csv.register_dialect('frq', delimiter='\t', quoting=csv.QUOTE_NONE)
with open('corrected.txt', 'w', newline='') as f:
    writer = csv.writer(f, dialect='frq')
    for row in output_data:
        writer.writerow(row)