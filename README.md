# TripAdvisor Dataset

## Overview
This repository contains a dataset of hotel reviews and ratings collected from TripAdvisor, which has been processed. The dataset includes reviews of various hotels along with metadata such as multiple-aspect ratings and review texts.

## Source
The data was originally distributed by Jiwei Li et al. (2013) and is hosted on his website [http://www.cs.cmu.edu/~jiweil/html/hotel-review.html](http://www.cs.cmu.edu/~jiweil/html/hotel-review.html) at Carnegie Mellon University.

## Processing
For details on how we processed the dataset, please refer to the [\`process.ipynb\`](https://github.com/jniimi/tripadvisor_dataset/blob/main/process.ipynb) file. Essentially, we used machine learning to extract posts where reviews are written in English. Specifically, we adopted \`fastText\`　([https://fasttext.cc](https://fasttext.cc)) by Meta, utilizing the pre-trained model [\`lid.176.bin\`](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

## Dataset Description
The contents of the two datasets (.csv and .pkl) are same; however, we recommend using pickle file (.pkl) which retains information on pandas variable types and np.nan for missing values, especially datetime. In the original data, the various variables were stored in JSON format, but we have reorganised them so that the reviews and ratings are combined in one line as a pandas data set.

The dataset includes the following columns in each line:
- `hotel_id`: Unique identifier for hotels.
- `user_id`: Unique identifier for users.
- `title`: Heading of the user review.
- `text`: Actual text of the review.
- `review`: reviews combined as follows: `title` \n `text`
- `overall`: The rating given by the user.
- `cleanliness`: The rating regarding the cleanliness.
- `value`: The rating regarding the value.
- `location`:  The rating regarding the location.
- `rooms`:  The rating regarding the rooms.
- `sleep_quality`:  The rating regarding the sleep quality.
- `date_stayed`: The date when the user stayed.
- `date`: The date when the review was posted.

## Usage
Our actual dataset is stored in Huggingface Dataset so that you need to install `datasets` package as follows:
```bash
pip install datasets
```
You can load the dataset with `datasets` package and easily convert to `pd.DataFrame` as:
```python
from datasets import load_dataset
df = load_dataset("jniimi/tripadvisor-review-rating")
df = df['train'].to_pandas()
```
or perhaps grabbing the pickle file as:
```python
import pandas as pd
from huggingface_hub import hf_hub_download
f = hf_hub_download('jniimi/tripadvisor-review-rating', repo_type='dataset', filename='data.pkl')
df = pd.read_pickle(f)
```

However, the whole dataset is huge so that you can also use the sampled data with 1000 observations file ([https://huggingface.co/datasets/jniimi/tripadvisor-review-rating/resolve/main/data1000.pkl](https://huggingface.co/datasets/jniimi/tripadvisor-review-rating/resolve/main/data1000.pkl)) as follows (e.g., using google colab):
```python
import pandas as pd
from huggingface_hub import hf_hub_download
f = hf_hub_download('jniimi/tripadvisor-review-rating', repo_type='dataset', filename='data1000.pkl')
df = pd.read_pickle(f)
```

## Citation
As indicated earlier, this dataset is a reprocessed distribution of a published dataset by Dr. Li, so please follow their instructions for use.

### 1. Original Dataset
Do not forget to cite the original Hotel Dataset (Li et al., 2013) [https://nlp.stanford.edu/~bdlijiwei/Code.html](https://nlp.stanford.edu/~bdlijiwei/Code.html)
```bibtex
@inproceedings{li2013identifying,
  title={Identifying manipulated offerings on review portals},
  author={Li, Jiwei and Ott, Myle and Cardie, Claire},
  booktitle={Proceedings of the 2013 conference on empirical methods in natural language processing},
  pages={1933--1942},
  year={2013}
}
```
Li, J., Ott, M., & Cardie, C. (2013, October). Identifying manipulated offerings on review portals. In Proceedings of the 2013 conference on empirical methods in natural language processing (pp. 1933-1942). [https://aclanthology.org/D13-1199/](https://aclanthology.org/D13-1199/)

### 2. Citation for us
Our dataset will soon be citable in academic publications as well.
```bibtex
@misc{tripadvisor_dataset,
author = {Junichiro, Niimi},
title = {Hotel Review Dataset (English)},
year = {2024},
howpublished = {\url{https://github.com/jniimi/tripadvisor_dataset}}
}
```
