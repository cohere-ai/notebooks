from fastapi import FastAPI
from pydantic import BaseModel, conlist
import cohere
from cohere import ClassifyExample

# Setup the Cohere client
co = cohere.Client("COHERE_API_KEY") # Get your API key here: https://dashboard.cohere.com/api-keys

app = FastAPI()

class ProductReviews(BaseModel):
    reviews: conlist(str, min_length=1)

@app.post("/prediction")
def predict_sentiment(product_reviews: ProductReviews):
    examples=[ClassifyExample(text="The order came 5 days early", label="positive"), 
            ClassifyExample(text="The item exceeded my expectations", label="positive"), 
            ClassifyExample(text="I ordered more for my friends", label="positive"), 
            ClassifyExample(text="I would buy this again", label="positive"), 
            ClassifyExample(text="I would recommend this to others", label="positive"), 
            ClassifyExample(text="The package was damaged", label="negative"), 
            ClassifyExample(text="The order is 5 days late", label="negative"), 
            ClassifyExample(text="The order was incorrect", label="negative"), 
            ClassifyExample(text="I want to return my item", label="negative"), 
            ClassifyExample(text="The item's material feels low quality", label="negative"), 
            ClassifyExample(text="The item was nothing special", label="neutral"), 
            ClassifyExample(text="I would not buy this again but it wasn't a waste of money", label="neutral"), 
            ClassifyExample(text="The item was neither amazing or terrible", label="neutral"), 
            ClassifyExample(text="The item was okay", label="neutral"), 
            ClassifyExample(text="I have no emotions towards this item", label="neutral")]
    
    response = co.classify(
        inputs=product_reviews.reviews,
        examples=examples)

    return response.classifications