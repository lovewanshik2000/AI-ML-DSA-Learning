from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the trained model once at startup
with open("model_final.pkl", "rb") as file:
    clf = pickle.load(file)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict_result(request: Request, cgpa: float = Form(...), iq: float = Form(...)):
    # Input validation
    if not (0 < cgpa <= 10):
        error_msg = "Please enter a valid CGPA between 0 and 10."
        return templates.TemplateResponse("index.html", {"request": request, "error": error_msg})

    if not (50 <= iq <= 200):
        error_msg = "Please enter a valid IQ between 50 and 200."
        return templates.TemplateResponse("index.html", {"request": request, "error": error_msg})

    # Prepare the input features
    features = np.array([[cgpa, iq]])
    prediction = clf.predict(features)[0]
    print(f"Received CGPA: {cgpa}, IQ: {iq}, Prediction: {prediction}")

    # Interpret the prediction
    if prediction == 1:
        result = "🎉 Placement ho jayega!"
    else:
        result = "😔 Placement nahi hoga."

    # Render result page
    return templates.TemplateResponse("result.html", {
        "request": request,
        "cgpa": cgpa,
        "iq": iq,
        "result": result
    })
