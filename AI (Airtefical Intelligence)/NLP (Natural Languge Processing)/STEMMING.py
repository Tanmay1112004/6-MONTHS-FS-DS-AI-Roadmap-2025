import nltk
from nltk.stem import PorterStemmer

#using porter stemmer you can always stem the word called from PorterStemmer 
#poterstemmer librarty will help you to find the root word 

from nltk.corpus import stopwords

#STOPWORDS – stopwords are present inside the nltk.corpus 
#why we use stopwords hear becuase if you see below para then we do see some word called of, the, and , our, of , them 
#this kind of words are repeted again and again & these words are no such a meaningfull information & there is no meaning when we assign to the computer or machine
#stopwords help us to remove this kind of words in the paragraph for better text preprocessing
#most of the senario we do apply stopwords

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
                          
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()
#import stopwords
# I want to remove all the stopwords from my senterences 
# if you check the stopwords.words('english') you get a list of word which is not at all value to the paragraph
# you do get stopwords in many language. 
# after removing the stopwords i am going to stem the words by using portstemmer

# using for loop for all of sentences & using word_tokenize will convert all sentences to words
# basically i am writhing for word in words and i am taking from unique word from stopword.english
# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)   
    
    
    
    
    
    
    
    
    
    