import pandas as pd
#from pyexpat import features

#from sklearn.externals.array_api_compat.torch import result_type
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

data = pd.read_csv("spam.csv")

data.drop_duplicates(inplace=True)

data["Category"] = data["Category"].replace(["ham", "spam"], ["Not spam", "spam"])

mess = data["Message"]
cat = data["Category"]

(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess,cat,test_size=0.2)
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

#creating model

model = MultinomialNB()
model.fit(features,cat_train)

#test our model

features_test = cv.transform(mess_test)
#print(model.score(features_test,cat_test))

#predict data
def predict(message):
    input_message = cv.transform([message]).toarray()
    result =  model.predict(input_message)
    return result



st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detector")
st.markdown("### Check whether a message is Spam or Not Spam")

st.divider()

input_mess = st.text_area(
    "Enter your message",
    height=150,
    placeholder="Type your message here..."
)

if st.button("🔍 Analyze Message", use_container_width=True):

    if input_mess.strip():

        output = predict(input_mess)

        if output[0] == "spam":
            st.error("🚨 This message is SPAM")
        else:
            st.success("✅ This message is NOT SPAM")

    else:
        st.warning("⚠️ Please enter a message")


