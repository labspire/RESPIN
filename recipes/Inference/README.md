## Fairseq Inferencing
Inference script for finetuned Wav2vec2.0 model.

## Usage
* Activate the conda environment.
```bash
conda activate env_name
```
* Use the [fairseq_preprocessing](https://github.com/Amartyaveer/NLTM-Spire/blob/main/recipes/fairseq_preprocessing/) scripts to prepare the data.
* Note that the input is expected to be single channel, sampled at 16 kHz
* Things to be updated in the inference script(infer_d2v.sh):
```bash
* Update the infer.py script path to the fairseq directory.
* Update the metrics.py script path to the fairseq_preprocessing directory.

subset <train/valid/test>
w2v2_path <path to the finetuned model>
data_dir <path to the data directory>
results <path to the results directory>
dialect_level_ed <True/False> (if True, it will calculate the dialect level wer)
```
* The script will infer on the data and saves the `references` and its corresponding `hypothesis`. It also gives the `wer` and `cer` and saves it in the results directory specified in infer.sh script.

* This inference script uses the [`metrics.py`](https://github.com/Amartyaveer/NLTM-Spire/tree/main/recipes/fairseq_preprocessing) script to calculate the `wer` and `cer` from the saved `references` and `hypothesis` file.

* Run the inference script as follows:
```bash
./infer_d2v.sh --tags <tags> --gpu <gpu_id>
```

## Example

```bash
./infer_d2v.sh --tags 'mt hi en' --gpu 0
```

## References
1. Fairseq [data2vec](https://github.com/facebookresearch/fairseq/blob/main/examples/data2vec/README.md)