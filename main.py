from fastapi import FastAPI, HTTPException, Path
import json
app = FastAPI()


def load_data():
    with open("expenses.json", "r") as f:
        data = json.load(f)
    return data



@app.get("/")
def view():
    return {"Hello amar Ammu"}

@app.get("/view/{expense_id}")
def view_expenses(expense_id:str = Path(..., description="The ID of the expense to retrieve", example="1")):
    data = load_data()
    if expense_id in data:
        return data[expense_id]
    else:
        raise HTTPException(status_code=404, detail="Expense not found")