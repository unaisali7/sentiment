import streamlit as st 
import joblib
#load the trainde model
model = joblib.load("sentiment-model.pkl")
#define sentimental labels
sentiment_labels={'1':"positive","0":"negative"}
#create streamlit app
st.title("Sentimental analysis")

#import text area
user_input=st.text_area("enter your text")
#prediction button
if st.button("predict"):
    #perform sentiment prediction
    predictecd_sentiment = model.predict([user_input])[0]
    predictecd_sentiment_label = sentiment_labels[str(predictecd_sentiment)]

    #dislpay predict sentiment
    st.info(f"predicted Sentiment: {predictecd_sentiment_label}")