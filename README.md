<p align="center">
    <br>
    <img src="https://github.com/44himanshu44/Covid19-Question-and-Answering-system/blob/master/docs/who-emblem.png" width="400"/>
    <br>
</p>

<h2 align="center">
<p>Covid19 Question and Answering system on WHO document</p>
</h2>




![page_2](https://github.com/44himanshu44/Covid19-Question-and-Answering-system/blob/master/docs/corona_qna.gif) <br>


Using pretrained Allennlp Model bidaf-elmo-model-2020 for machine comprehension


## 📖 Contents
- [Dependencies](#Dependencies)
- [Dataset](#Dataset)


## Dependencies

Make sure you have:

* Python >= 3.6
* allennlp
* allennlp-models
* torch
* flask

Make sure you install torch version<=1.6.0 and >=1.5.0 through conda or pip, else the model won't run.
```python
conda install pytorch==1.6.0 torchvision==0.7.0 cpuonly -c pytorch

```
After installing torh simply run the below command
``` python
pip install allennlp==1.0.0 allennlp-models==1.0.0

```

## 📖Note
The python script downloads the model from google storage, if you want to run the script multiple times
you can download the model in zip format from [here](https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz) and set the path accordingly


## 📖Dataset
Any text format data can be used
<br>

## Clone this repository and run on command line:
```python
E:\Jupyter\Projects\QnA> python main.py
```


