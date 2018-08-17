import os
import json
from .translation import trans_dict
from .generate_json import generate_json
from ..util.check_input import verify_data_dir,  choose_json_dir


def run_dream(study_path, bids_path, log_path, json_path, subjects):
    d = dict()
    d["source_study_dir"] = study_path
    d["target_study_dir"] = bids_path
    d["log_dir"] = log_path
    d["ses_info_dir"] = json_path
    subj_dict = dict() 
    for subject in subjects:
        subj_dict[subject] = subject + ".json"
    d["ses_files"] = subj_dict
    with open(os.path.join(json_path, "bxh2bids_hopes_dreams.json"), "w") as f:
        json.dump(d, f)


def run_all(subjects, session, study_path, trans_file, json_path, bids_path, log_path):

    msg = verify_data_dir(study_path) 
    if msg:
        print("Error in folder check: " + msg) 
        return

    if not choose_json_dir(json_path):
        print("Please rerun the script with a different json output path!")
        return
        
    for subject in subjects:
        generate_json(subject, session, study_path + "data/", trans_dict(trans_file, subject, study_path + "Data/"), json_path)

    run_dream(study_path, bids_path, log_path, json_path, subjects)
    
