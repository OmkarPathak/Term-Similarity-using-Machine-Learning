# Term-Similarity-using-Machine-Learning
This is a small project to find similar terms in corpus of documents.

For the project I have used some tags based on news articles. These tags are extracted from various news aggregation methods. You can easily create custom dataset using the `create_dataset.py`

# How to Use

* Clone the Repository:

    `git clone https://github.com/OmkarPathak/A-Simple-Note-Taking-Web-App.git`

* Install the dependencies by simply executing:

    `pip3 install -r requirements.txt`

* Run the Term Similarity:

    `python3 find_word_similarity.py <word_to_search_for_similar_words>`

# Results

```bash

# Suppose you have to find the similar terms for the word 'machine learning'
# Then run the following command
$python3 find_word_similarity.py 'machine learning'

# Output would be

   distance                     name
0  0.000000         Machine Learning
1  0.000000         machine learning
2  1.213289                 software
3  1.213289                 Software
4  1.216590  Artificial Intelligence
5  1.216590  artificial intelligence
6  1.219796     predictive analytics
7  1.224047         data & analytics
8  1.224047           data analytics
9  1.241769       big data analytics

```

Built with ♥ by [`Omkar Pathak`](http://www.omkarpathak.in/)

# Donation

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

| PayPal | <a href="https://paypal.me/omkarpathak27" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| ₹ (INR)  | <a href="https://www.instamojo.com/@omkarpathak/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a> |
