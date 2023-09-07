# AVIBRIEF: Automated Vocal Informational Briefings Dataset 

**Description:** 
AVIBRIEF is a dataset designed to advance research in ASR and NLP tasks within the aviation domain. This dataset of aviation weather briefings includes 400 audio utterances spanning a duration of approximately 3.8 hours of ATIS, AWOS and ASOS audio from 197 different US airports, captured using a variety of collection methods including radio scanners, telephone calls,and aircraft radio systems. The audio files are accompanied by human annotated and verified transcripts. In addition, gold annotations of the transcript text are also provided for Named Entity Recognition (NER) tasks. The NER task involves identification of key information in the text and classification into a set of predefined categories. (e.g.: recognizing the correct digits for altimeter settings in an ATIS broadcast).

**Availability:** Thank you for your interest in this dataset. This dataset will be published on this site towards the **end of September 2023**.
The AVIBRIEF dataset can be downloaded from this link:
```
{LINK WILL BE AVAILABLE SOON}
```

![image](https://github.com/cirrusaircraft/avibrief-dataset/assets/137824085/6e5938ee-d5a3-4ee5-9401-9bc0011b43f8)


**Directory Structure:**
The AVIBRIEF dataset comprises of three subsets: i) WS (whole set) audio corpus contains all the 400 audio recordings and their transcripts, ii) SS (segmented set) segmented audio corpus derived from the source 400 files by segmenting the audio files into smaller duration. It consists of 882 audio files and their transcripts, iii) NS (NER set) NER dataset that contain only the 400 transcript files from WS with NER annotation labels. Each of these sets contain subsets for training, validation, and testing/evaluation (train,val,test) of asr and ner models. The directory structure of the zip file is listed below.
```
avibrief-dataset/
├── audio/
│   ├── ss_test/
│   │   └── 186 .wav files
│   ├── ss_train/
│   │   └── 599 .wav files
│   ├── ss_val/
│   │   └── 97 .wav files
│   ├── ws_test/
│   │   └── 84 .wav files
│   ├── ws_train/
│   │   └── 272 .wav files
│   ├── ws_val/
│   │   └── 44 .wav files
├── configs/
│   ├── conformer_ctc_bpe.yaml
│   └── small_conformer_ctc_bpe.yaml
├── manifest_files/
│   ├── ss_test_manifest.json
│   ├── ss_train_manifest.json
│   ├── ss_val_manifest.json
│   ├── ws_test_manifest.json
│   ├── ws_train_manifest.json
│   └── ws_val_manifest.json
├── ner/
│   ├── ns_test.conll
│   ├── ns_train.conll
│   └── ns_val.conll
├── preparation_script.py
├── README.md
└── LICENSE

```

**SETUP**

If users of this dataset would like to train or evaluate with [NVIDIA NeMo: an conversational AI toolkit](https://developer.nvidia.com/nemo), they will need to configure the paths in the manifest files to be absolute paths. This can be done by running the preparation script. 
To do so, cd into avibrief-dataset/ and run:
```
python3 preparation_script.py
```
This will change the '*' character in the manifest file to the absolute current working directory that the script is run from. 


**Data formats**

*Audio:*

Audio files are provided in sampled to 16000Hz, 16bit mono '.wav' files. The filenames for the audio files are of the following format:
{scanner or plane recorded}\_{ATIS/ASOS/AWOS}\_{airport identifier}\_{subset}\_{unique number id}.wav
If there is no prefix 'scanner' or 'plane', then the audio was recorded from phone loopback recording.

*Manifest / Transcript format:*

Each line in the Nemo ASR manifest format is a json element with audio_filepath, text, and duration.

Example of line from AVIBRIEF dataset in NeMo ASR manifest format:
```
{"audio_filepath": "*/audio/ws_train/AWOS_dlh_train_8.wav", "duration": 34.62695726706858, "text": "duluth international airport automated weather observation one four five two zulu wind zero five zero at one three visibility one quarter snow freezing fog sky condition vertical visibility niner hundred temperature minus zero six celsius dew point minus zero eight celsius altimeter two niner seven niner remarks tower visibility one quarter density altitude minus five hundred"}
```
---
*Named Entity Recognition:*

<!--files for training are provided in folder..... in format... complete token list is given in the paper...-->
Data for Named Entity Recognition are provided in CoNLL-2003 format (.conll extension). These files can be found in the ``avibrief-dataset/ner/`` directory, each with the prefix of 'ns'(ns_train.conll, ns_val.conll, ns_test.conll). 

Each row of a conll file contains four columns separated by a single space. Each column corresponds to the token, part-of-speech(POS) tag, syntactic chunk tag, and the last column contains the named entity tag. In our case we opted to not use the second and third columns and chose to just use the fourth column. As such, the second column contains just '-X-', and the third column contains '_' place holder character. 

CoNLL-2003 file excerpt:

```
duluth -X- _ B-LOC
international -X- _ I-LOC
airport -X- _ I-LOC
information -X- _ O
foxtrot -X- _ B-PHONETIC
one -X- _ B-TIME
five -X- _ I-TIME
five -X- _ I-TIME
five -X- _ I-TIME
zulu -X- _ O
...
```

A complete list of tokens and their corresponding representations can be found in our paper: >``AVIBRIEF: Automated Vocal Informational Briefings Dataset`` Which can be found in IEEE under DASC 2023

**Using this dataset**

Audio files in this dataset can be used for ASR model development and evaluation. Our paper results were achieved using NVIDIA NeMo:
NVIDIA NeMo is a powerful toolkit for ASR and NLP models and pipelines. To find out more read the User Guide to get started: 
https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/index.html

Tutorials for training and evaluation of Word-Error-Rate can also be found at the [NeMo repo](https://github.com/NVIDIA/NeMo) under 
``<NeMo_git_root>/tutorials/ASR``.

The Conll files can be used for development and evalutation of NER models that extract the specific weather elements of the briefings.

One package that we reccommend be used for NER training and evaluation(F1 scores) is spaCy. Documentation for using spaCy can be found here: https://spacy.io/usage

**Config files**

The training parameters are defined in the config (.yaml)files under ``avibrief-dataset/configs/``.
The config files included for small and large conformer models were modified from the config files that are provided in the [NeMo repo r1.16.0](https://github.com/NVIDIA/NeMo/tree/r1.16.0) at `` <NeMo_git_root>/examples/asr/conf/conformer/conformer_ctc_bpe.yaml``
The set of optimal parameters may differ from what we have chosen, and may differ if additions are made to the data used for training.

**Conformer model NGC links**

These are links to the pretrained Conformer models used in our original paper.

[Conformer Large (version 1.10.0)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_en_conformer_ctc_large)

[Conformer Small (version 1.6.0)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_en_conformer_ctc_small)

For questions contact Andrew Johnson: adjohnson@cirrusaircraft.com
