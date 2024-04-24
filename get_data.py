from datasets import load_dataset

def load_data():
    '''
    Before running this function, you need to install datasets package.
    '''
    data = load_dataset('jniimi/tripadvisor-review-rating')
    return data

if __name__ == '__main__':
    data = load_data()
