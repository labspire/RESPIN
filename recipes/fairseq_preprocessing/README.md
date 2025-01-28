## Data Preparation
The script `run_data_prep.sh` is used for preparing the data as required by the fairseq.
* You need to prepare the files in [kaldi format](https://kaldi-asr.org/doc/data_prep.html). The script will convert the kaldi format to fairseq format.
* The following files are required in the kaldi format:
```
wav.scp (contains the utterance id and the path to the wav file)
text (contains the utterance id and the transcript)
utt2dial (contains the utterance id and the dialect id) [optional]
```
## Usage
* Activate the conda environment.
```bash
conda activate env_name
```
* Things to be updated in the data preparation script(run_data_prep.sh):
```
pyscript <path to the data_prep.py script>

train_folder <path to the train folder>
dev_folder <path to the dev folder>
test_folder <path to the test folder>
output_folder <path to the output folder>

Make the train, dev, test flags 0/1 based on the requirements.

Also add/remove the arguments(--dialect_prep) in the data_prep.py script based on the requirements.
```

* This script will prepare the data in the fairseq format and store it in the output folder specified in the script.
```
.tsv (contains the path to the wav file \t number of samples)
.ltr (contains the transcript)
.wrd (containes the character space separated and words | seperated for the transcript)
.dict.ltr.txt (contains the character dictionary \t frequency)
lexicon.lst (contains the word dictionary \t space separated characters)

.tsv, .ltr, .wrd files have the same corresponding index.
```

* Run the inference script as follows:
```bash
./run_data_prep.sh --tags <tags>
```

## Example

```bash
./run_data_prep.sh --tags 'mt hi en' 
```

## References
1. Fairseq [wav2vec 2.0](https://github.com/facebookresearch/fairseq/blob/main/examples/wav2vec/README.md)