# Intent Service

Chatterbox supports both Padatious and Adapt intent handlers. 
Chatterbox Core has an intent service that decides which intent will be triggered by a particular utterance. 
This is based on the confidence of a

## Intent Confidence

## Order of Priority
1. Active skills attempt to handle using `converse()`  
2. IntentBox
3. Fallbacks:  
  - General fallbacks  
  - Unknown intent handler  
