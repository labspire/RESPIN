## Single File Inferencing
Inference script for finetuned Wav2vec2.0 model on single audio file.

## Usage
* append fairseq path to sys.path in the `infer.py` script or add it to the PYTHONPATH environment variable.
```python
import sys
sys.path.append('<path_to_data2vec_aqc>')
```
```bash
export PYTHONPATH=$PYTHONPATH:<path_to_data2vec_aqc>
```
* update model path in the config.yaml
* update device('cpu', 'cuda') in the config.yaml
* run the infer.py script
* Note that the input is expected to be single channel, sampled at 16 kHz

## Example
```python
from infer import infer
output = infer(file_pth='test.wav', conf_pth='config.yaml')
```