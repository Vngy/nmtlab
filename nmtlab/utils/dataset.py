#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torchtext
from nmtlab.utils.vocab import Vocab


class MTDataset(object):
    """Bilingual dataset.
    """
    
    def __init__(self, corpus_path, src_vocab_path, tgt_vocab_path, batch_size=64, max_length=60):
        self._max_length = max_length
        self._batch_size = batch_size
        
        src = torchtext.data.Field(pad_token="<null>", preprocessing=lambda seq: ["<s>"] + seq + ["</s>"])
        src.vocab = Vocab(src_vocab_path)
        tgt = torchtext.data.Field(pad_token="<null>", preprocessing=lambda seq: ["<s>"] + seq + ["</s>"])
        tgt.vocab = Vocab(tgt_vocab_path)
        
        self.train_data = torchtext.data.TabularDataset(
            path=corpus_path, format='tsv',
            fields=[('src', src), ('tgt', tgt)],
            filter_pred=self._len_filter
        )
        
    def _len_filter(self, sample):
        return len(sample.src) <= 60 and len(sample.tgt) <= 60
    

