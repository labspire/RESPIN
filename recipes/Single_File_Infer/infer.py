import sys
sys.path.append('/home1/data2vec-aqc')
from examples.speech_recognition.w2l_decoder import W2lViterbiDecoder
from examples.data2vec.models.data2vec_audio import Data2VecAudioModel # required import for loading model
import torchaudio
import yaml
import argparse
import fairseq
import torch
import re
import soundfile as sf
import os
from tqdm import tqdm

args, model, generator, task = None, None, None, None

def load_config(conf):
    global args
    # reading config
    with open(conf) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    args = argparse.Namespace(**config)

def load_model(mdl_pth, device):
    global model, generator, task
    model, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([mdl_pth])
    model = model[0].to(device)
    generator = W2lViterbiDecoder(args, task.target_dictionary)

# use viterbi decoder
def decode(inp):
    model.eval()
    try:
        encoder_out = model(**inp, features_only=True)
        emm = model.get_normalized_probs(encoder_out, log_probs=True)
        emm = emm.detach().cpu().float()
        emm = emm.transpose(0, 1)
        out = generator.decode(emm)
        text=""
        for i in out[0][0]['tokens']:
            text+=task.target_dictionary[i]
        return text
    except:
        return "**Error**"

def get_data(file, device):
    wav, sr = sf.read(file)
    if sr != 16000:
        wav = torchaudio.transforms.Resample(sr, 16000)(wav)
    inp = {'source': [torch.tensor(wav, dtype=torch.float32).unsqueeze(0).to(device),
                      torch.tensor(wav, dtype=torch.float32).unsqueeze(0).to(device)],
            'padding_mask':torch.zeros(wav.shape[-1]).to(device)}
    return inp

def write_file(file, text):
    with open(file, 'a') as f:
        f.write("%s\n" % text)

def infer(file_pth, conf_pth):
    load_config(conf_pth)
    load_model(args.model, args.device)
    inp = get_data(file_pth, args.device)
    out = decode(inp)
    return out.replace("|", " ")





