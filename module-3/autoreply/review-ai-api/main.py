from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

# load your trained model
tokenizer = BertTokenizer.from_pretrained("../final-model")
model = BertForSequenceClassification.from_pretrained("../final-model")

class ReviewRequest(BaseModel):
    review: str

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    return pred


@app.post("/predict")
def get_reply_api(req: ReviewRequest):
    sentiment = predict_sentiment(req.review)

    if sentiment == 0:
        reply = "We’re sorry for your experience. We will improve our service."
    else:
        reply = "Thank you for your valuable feedback!"

    return {
        "review": req.review,
        "sentiment": sentiment,
        "reply": reply
    }