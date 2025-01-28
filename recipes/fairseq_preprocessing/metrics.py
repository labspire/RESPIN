import jiwer
import os, sys, re
from pathlib import Path
import ast

def read_files_for_dialect(folder, subset_path, dialect_path):
  
    assert os.path.exists(os.path.join(raw_data_folder, dialect_path))
    with open(os.path.join(raw_data_folder, dialect_path), 'r') as f:
        lines = f.read().split('\n')

    lines = {d.split('\t')[0]:d.split('\t')[1] for d in lines if len(d)>0}
    with open(os.path.join(raw_data_folder, subset_path+'.tsv'), 'r') as f:
        data = f.read().split('\n')[1:-1]
        
    data = [Path(l.split('\t')[0]).stem for l in data]
    return data, lines

def main():
    with open(os.path.join(folder, hyp_path), 'r') as f:
        hyps = f.read().split('\n')[:-1]
    with open(os.path.join(folder, ref_path), 'r') as f:
        refs = f.read().split('\n')[:-1]
    
    assert len(hyps) == len(refs)
    indices = [int(string[string.index('(None-'):].replace("(None-", "").replace(")", "").strip()) for string in hyps]
    refs = [re.sub("[\(\[].*?[\)\]]", "", l).strip() for l in refs]
    hyps = [re.sub("[\(\[].*?[\)\]]", "", l).strip() for l in hyps]
    wer = jiwer.wer(refs, hyps)
    cer = jiwer.cer(refs, hyps)
    save_folder = os.path.join(results_dump)
 
    if dialect_level_ed==True:
        ids, dialect_map = read_files_for_dialect(raw_data_folder, subset, 'utt2dialect_{}'.format(subset))
        dialect_level_files = {}
        for idx in range(len(hyps)):
            index = indices[idx]
            current_utt_id = ids[index]
            dialect = dialect_map[current_utt_id]
            if dialect not in dialect_level_files: dialect_level_files[dialect] = {'ref':[], 'hyp':[]}
            dialect_level_files[dialect]['ref'].append(refs[idx])
            dialect_level_files[dialect]['hyp'].append(hyps[idx])
        dialects = sorted(list(dialect_level_files.keys()))
        wers, cers = [], []
        for dialect in dialects:
            wer_ = jiwer.wer(dialect_level_files[dialect]['ref'], dialect_level_files[dialect]['hyp'])
            cer_ = jiwer.cer(dialect_level_files[dialect]['ref'], dialect_level_files[dialect]['hyp'])
            wers.append(str(wer_*100))
            cers.append(str(cer_*100))

    with open(os.path.join(save_folder, 'results'), 'a') as f:
        if dialect_level_ed==True:
            f.write('\t'.join([subset, kenlm.replace('.arpa', ''), str(wer*100), str(cer*100), *wers, *cers])+'\n')
        else:
            f.write('\t'.join([subset, kenlm.replace('.arpa', '') , str(wer*100), str(cer*100)])+'\n')
    
    
if __name__ == '__main__':
    assert len(sys.argv) == 8
    folder = sys.argv[1]
    subset = sys.argv[2]
    kenlm = Path(sys.argv[3]).stem
    results_dump = sys.argv[4]
    exp_tag = sys.argv[5]
    raw_data_folder = sys.argv[6]
    hyp_path = f'hypo.word-checkpoint_best.pt-{subset}.txt'
    ref_path = f'ref.word-checkpoint_best.pt-{subset}.txt'
    dialect_level_ed= ast.literal_eval(sys.argv[7])
    main()



