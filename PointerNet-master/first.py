import numpy as np
import pandas as pd
import csv

from decision_transformer.evaluation.evaluate_episodes import evaluate_episode, evaluate_episode_rtg
from decision_transformer.models.decision_transformer import DecisionTransformer
from decision_transformer.models.mlp_bc import MLPBCModel
from decision_transformer.training.act_trainer import ActTrainer
from decision_transformer.training.seq_trainer import SequenceTrainer



def backtrack(csv, track, len):
    
    if(len(track) == len):
        for i in range(len):
            csv.writerrow()
    
    for i in range(len):
        if i in track: 
            continue

        track.append(i)
        backtrack(res, track, len)
        track.pop()



if __name__ == '__main__':
    len = 100
    track, res =[], []

    f = open('news.csv', 'w', encoding='utf-8')
    #  2.基于文件对象构建csv写入对象
    csv_write = csv.writer(f)

    for data in data_list:
        #  4.写入csv文件
        csv_write.writerow([data['新闻标题'], data['发布时间'], data['新闻链接'], data['阅读次数'], data['新闻来源']])

    backtrack(res, track, len)
    

