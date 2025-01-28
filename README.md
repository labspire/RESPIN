## Demo
[Coming Soon...]()

## Models

The WERs specified are without the use of any language model.

Model | Pre-training data | Fine-tuning data | Model Links | WER (test-RESPIN) | CER (test-RESPIN)
|---|---|---|---|---|---
data2vec-aqc | --- | Bhojpuri | [fairseq](https://huggingface.co/SpireLab/RESPIN/resolve/main/finetuned/data2vec-aqc/bh_checkpoint_best.pt) | 14.628 | 3.794


* finetuning procedures can be found [here]().
* Inference procedures can be found [here]().
<!-- * Single file inference procedures can be found [here]() -->

## Directory Structure
```
RESPIN
├── configs
│   └── finetuned ── data2vec-aqc.yaml
├── data
│   ├── examples
│   └── bh
├── models
│   ├── finetuned
│   │   └── indic_finetuned
│   └── pretrained
├── recipes
│   ├── Training
│   │   └── train.sh
│   ├── Inference
│   │   └── infer.sh
│   └── fairseq_preprocessing
│       ├── data_prep.py
│       ├── metrics.py
│       └── run_data_prep.sh
├── requirements.txt
└── README.md
```

## Requirements and Installation
* Create a new conda environment:
```bash
conda create -n env_name python=3.10
conda activate env_name
```
* Python version >= 3.10
* [PyTorch](https://pytorch.org/) version >= 2.0.0
* Fairseq version >= 0.12.2
* CUDA >= 11.8
* For training new models, you'll also need an NVIDIA GPU and NCCL
* To install requirements:

```bash
pip install -r requirements.txt
```
* To install fairseq and develop locally:

``` bash
git clone https://github.com/Speech-Lab-IITM/data2vec-aqc
cd data2vec-aqc/
pip install --editable ./
```
* For faster training install NVIDIA's apex library:
```bash
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" \
  --global-option="--deprecated_fused_adam" --global-option="--xentropy" \
  --global-option="--fast_multihead_attn" ./
```
* For Augmentation to work install [torchaudio-augmentations](https://github.com/Speech-Lab-IITM/torchaudio-augmentations):
```bash
git clone https://github.com/Speech-Lab-IITM/torchaudio-augmentations
cd torchaudio-augmentations
pip install --editable ./ 
```

* Flashlight version >= 0.0.7
* To install [flashlight-text](https://github.com/flashlight/text) and [flashlight-sequence](https://github.com/flashlight/sequence)
```bash
pip install flashlight-text

git clone https://github.com/flashlight/sequence && cd sequence
pip install .
```
* To install parse_options:
```bash
wget https://raw.githubusercontent.com/kaldi-asr/kaldi/master/egs/wsj/s5/utils/parse_options.sh && sudo mv parse_options.sh /usr/local/bin/

```
<b>Required Step

Add the musan dataset path in: <br>
data2vec-aqc/fairseq/data/audio/raw_audio_dataset.py <br>
```python
path_to_musan_noise_set = 'path_to_musan_dataset'
```

* For musan dataset.
[Musan](https://www.openslr.org/resources/17/musan.tar.gz)


## Reference Code
1. Facebook AI Research Sequence-to-Sequence Toolkit written in Python. [fairseq](https://github.com/facebookresearch/fairseq)
2. SPRING-LAB ([data2vec_aqc](https://asr.iitm.ac.in/models))
3. OpenSLR [musan](https://www.openslr.org/17/)



