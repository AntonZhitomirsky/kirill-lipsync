# %%
import os, sys

# Add the setup_data_vars function as we will need it to find the directory for the training data.
dir1 = os.path.abspath(os.path.join(os.path.abspath(''), 'OpenVoice'))
if not dir1 in sys.path: sys.path.append(dir1)

import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter

# %%
os.environ['LD_LIBRARY_PATH']

# %%
ckpt_converter = '/home/avzh1/Documents/personal/kirill/lipsync/2023QinOpenvoice/OpenVoice/checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = '../outputs_v2_final'

tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)

# %% [markdown]
# If the below doesn't run because the kernel crashed, run the following in your command terminal:
# 
# `!find ~+/../../.venv/ -type f -name "libcudnn_ops_infer.so.8"`
# and copy everything before "libcudnn_ops_infer.so.8" after the colon:
# `!export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<<<WHAT YOU'VE COPIED>>>`

# %%
reference_speaker = '/home/avzh1/Documents/personal/kirill/lipsync/content/reference_voice_cropped.mp3'

target_se, audio_name = se_extractor.get_se(reference_speaker, tone_color_converter, vad=False)

# %%
target_se.shape, audio_name