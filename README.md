I have implemented 2 methods to predict partiality

1- Unigram and machine learning methods (message impartiality in social media discussions) [2016 paper]

We have human-annotated tweets on which we test our method for the accuracy score.
Run JSON.ipynb to understand coorelation between discernability of affilation of author the same as the classification of impartiality of tweet

To test method 1:

install python jupyter and numpy using pip. 
and run each cell of the following notebook : 

Unigram Method.ipynb
Give different tweets in cell 12 and check bias by running cell 13

Method2:
Run Classifier2.ipynb
It takes tweets from tweet_20.txt and predicts affiliation.
The confidence of predicting affiliation is considered as the partiality score


2 - Recognising Stance in online debates [2015 paper] - Open Stance recognition folder and do the following

1. To find target-opinion pair: First run "/Fir_Ie/Post/Find_Target_Opinion.py
   and then run "/Fir_Ie/Post/filter.py", and the output file is "Filter_Post_Only_Targt_opinion.txt"

2. Co-reference resolution: First run it("Coreference_stanford-corenlp/corenlp.py") in one terminal  and open anther terminal and run "Coreference_stanford-corenlp/client.py" output file is "final2_only_coref.txt"

3. Nagetion word: Run "Fir_Ie/Nagetion/nagetion.py" and output file "final_nagetion.txt"

4. Final classification: Run "Fir_Ie/RSOD_with_TF.py", here we need all the output files these are generated from the above. "Filter_Post_Only_Target_opinion.txt" is in the same format as in lel.txt

