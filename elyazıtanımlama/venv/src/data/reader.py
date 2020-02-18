
"""                      Dataseet okuma ve işleyiş
"""

import os
import html
import string
import xml.etree.ElementTree as ET

from data import preproc as pp
from functools import partial
from glob import glob
from multiprocessing import Pool


class Dataset():
    """gerçek görüntüleri ve cümleleri okumak için veri kümesi sınıfı (işlenmemiş dosyalar)"""

    def __init__(self, source, name):
        self.source = source
        self.name = name
        self.dataset = None
        self.partitions = ['train', 'valid', 'test']

    def read_partitions(self):
        """"Veri kümesinden görüntüleri ve cümleleri okur"""

        self.dataset = getattr(self, f"_{self.name}")()

    def preprocess_partitions(self, input_size):
        """Ön işlem görüntüleri ve bölümlerdeki cümleler"""

        for y in self.partitions:
            arange = range(len(self.dataset[y]['gt']))

            for i in reversed(arange):
                text = pp.text_standardize(self.dataset[y]['gt'][i])

                if not self.check_text(text):
                    self.dataset[y]['gt'].pop(i)
                    self.dataset[y]['dt'].pop(i)
                    continue

                self.dataset[y]['gt'][i] = text.encode()

            pool = Pool()
            self.dataset[y]['dt'] = pool.map(partial(pp.preprocess, input_size=input_size), self.dataset[y]['dt'])
            pool.close()
            pool.join()

    def _bentham(self):
        """Bentham dataset okunur"""

        source = os.path.join(self.source, "BenthamDatasetR0-GT")
        pt_path = os.path.join(source, "Partitions")

        paths = {"train": open(os.path.join(pt_path, "TrainLines.lst")).read().splitlines(),
                 "valid": open(os.path.join(pt_path, "ValidationLines.lst")).read().splitlines(),
                 "test": open(os.path.join(pt_path, "TestLines.lst")).read().splitlines()}

        transcriptions = os.path.join(source, "Transcriptions")
        gt = os.listdir(transcriptions)
        gt_dict = dict()

        for index, x in enumerate(gt):
            text = " ".join(open(os.path.join(transcriptions, x)).read().splitlines())
            text = html.unescape(text).replace("<gap/>", "")
            gt_dict[os.path.splitext(x)[0]] = " ".join(text.split())

        img_path = os.path.join(source, "Images", "Lines")
        dataset = dict()

        for i in self.partitions:
            dataset[i] = {"dt": [], "gt": []}

            for line in paths[i]:
                dataset[i]['dt'].append(os.path.join(img_path, f"{line}.png"))
                dataset[i]['gt'].append(gt_dict[line])

        return dataset


    def check_text(text):
        """metnin noktalama işaretleri yerine daha fazla karaktere sahip olduğundan emin olma..."""

        strip_punc = text.strip(string.punctuation).strip()
        no_punc = text.translate(str.maketrans("", "", string.punctuation)).strip()

        if len(text) == 0 or len(strip_punc) == 0 or len(no_punc) == 0:
            return False

        punc_percent = (len(strip_punc) - len(no_punc)) / len(strip_punc)

        return len(no_punc) >= 2 and punc_percent <= 0.1
