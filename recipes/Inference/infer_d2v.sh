#!/bin/bash
set -e
tags='bh'
gpu=0
. parse_options.sh
export CUDA_VISIBLE_DEVICES=$gpu
subset="test"
dialect_level_ed=False

for tag in $tags; do 
w2v2_pth="/fairseq/Models/finetuned/data2vec_aqc_finetuned/${tag}_checkpoint_best.pt"
data_dir="/fairseq/data/processed_${tag}"    #####
results="/fairseq/results/${tag}/"   #####

[ -e $results/${tag}/hypo.units-checkpoint_best.pt-test.txt ] && rm $results/${subset}/${tag}/*.txt
[ -e $results/{tag}/hypo.units-checkpoint_best.pt-valid.txt ] && rm $results/${subset}/${tag}/*.txt

python3 data2vec-aqc/examples/speech_recognition/new/infer.py \
    task=audio_finetuning \
    task.data=$data_dir \
    common.user_dir=data2vec-aqc/examples/data2vec \
    decoding.results_path=$results/${subset}/${tag} \
    decoding.type=viterbi \
    decoding.silweight=0 \
    decoding.unique_wer_file=True \
    dataset.gen_subset=$subset  \
    common_eval.path=$w2v2_pth \
    decoding.beam=1 

python3 fairseq_preprocessing/metrics.py $results/${subset}/${tag} $subset viterbi_${tag} $results $tag ${data_dir} $dialect_level_ed

done