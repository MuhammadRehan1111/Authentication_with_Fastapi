import json,os
from typing import Dict,List

User_File= "user.json"
Analysis_File= "analysis.json"

def load_data(file_path:str):
    if os.path.exists(file_path):
        with open(file_path,"r") as f:

            return json.load(f)

    return {}

def save_data(file_path:str,data):
    with open (file_path,"w") as f:
        json.dump(data,f,indent=4)


@app.get("/")
def get_all_user():
    return load_data(User_File)


@app.get("/User_id/{user_id}")
def get_user_by_id(user_id:str):
    user=user.load(User_File)
    return user.get(user_id)


@app.get("/user/{user_id}/analysis")
def get_user_by_id(email:str):
    user= load_data(User_File)
    for user in user.values():
        if user["email"]==email:
            return user
    return None


@app.post("/create_user")
def create_user(user_id:str,user_data:dict):
    user=load_data(User_File)
    user[user_id]=user_data
    save_data(User_File,users)


@app.delete("/detele_user/{user_id}")
def delete_user(user_id:str):
    user=load_data(User_File)
    if user_id in user:
        del user[user_id]
        save_data(User_File,user)
        return True
    return False


def save_analysis(analysis_id:str,analysis_data:dict):
    analysis=load_data(Analysis_File)
    analysis[analysis_id]=analysis_data
    save_data(Analysis_File,analysis)

@app.get_analysis("/analysis/{analysis_id}")
def get_user_analyses(user_id: str):
    analyses = load_data(ANALYSIS_FILE)
    return [a for a in analyses.values() if a["user_id"] == user_id]