# TripAdvisor Dataset

## Overview
This repository contains a dataset of hotel reviews and ratings collected from TripAdvisor, which has been processed. The dataset includes reviews of various hotels along with metadata such as multiple-aspect ratings and review texts.

## Source
The data was originally distributed by Jiwei Li et al. (2013) and is hosted on his website [http://www.cs.cmu.edu/~jiweil/html/hotel-review.html](http://www.cs.cmu.edu/~jiweil/html/hotel-review.html) at Carnegie Mellon University.

## Processing
For details on how we processed the dataset, please refer to the [\`get_data.ipynb\`](https://github.com/jniimi/tripadvisor_dataset/blob/main/get_data.ipynb) file. Essentially, we used machine learning to extract posts where reviews are written in English. Specifically, we adopted \`fastText\`　([https://fasttext.cc](https://fasttext.cc)) by Meta, utilizing the pre-trained model [\`lid.176.bin\`](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

## Dataset Description
The contents of the two datasets (.csv and .pkl) are same; however, we recommend using pickle file (.pkl) which retains information on pandas variable types and np.nan for missing values, especially datetime. In the original data, the various variables were stored in JSON format, but we have reorganised them so that the reviews and ratings are combined in one line as a pandas data set.

The dataset includes the following columns in each line:
- `hotel_id`: Unique identifier for hotels.
- `user_id`: Unique identifier for users.
- `title`: Heading of the user review.
- `review`: Actual text of the review.
- `overall`: The rating given by the user.
- `cleanliness`: The rating regarding the cleanliness.
- `value`: The rating regarding the value.
- `location`:  The rating regarding the location.
- `rooms`:  The rating regarding the rooms.
- `sleep_quality`:  The rating regarding the sleep quality.
- `date_stayed`: The date when the user stayed.
- `date`: The date when the review was posted.

## Usage
As indicated earlier, this dataset is a reprocessed distribution of a published dataset by Dr. Li, so please follow their instructions for use.

### Original Dataset
Do not forget to cite the original Hotel Dataset (Li et al., 2013) [https://nlp.stanford.edu/~bdlijiwei/Code.html](https://nlp.stanford.edu/~bdlijiwei/Code.html)

### Citation for us
Our dataset will soon be citable in academic publications as well.
```
@misc{tripadvisor_dataset,
author = {Junichiro, Niimi},
title = {Hotel Review Dataset (English)},
year = {2024},
howpublished = {\url{https://github.com/jniimi/tripadvisor_dataset}}
}
```

## References
Li, J., Ott, M., & Cardie, C. (2013, October). Identifying manipulated offerings on review portals. In Proceedings of the 2013 conference on empirical methods in natural language processing (pp. 1933-1942). [https://aclanthology.org/D13-1199/](https://aclanthology.org/D13-1199/)