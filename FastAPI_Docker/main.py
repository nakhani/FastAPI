from fastapi import FastAPI, File, Form, HTTPException, Path
import sqlite3

app = FastAPI()

def get_db():
    try:
        con = sqlite3.connect("todo.db")
        con.row_factory = sqlite3.Row 
        return con
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.get("/items")
def read_root():
    con = get_db()
    if con:
        my_cursor = con.cursor()
        result = my_cursor.execute("SELECT * FROM tasks")
        tasks = result.fetchall()
        con.close()
        return [dict(task) for task in tasks] 
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database")

@app.post("/items")
def add_root(title: str = Form(), description: str = Form(), time: str = Form()):
    con = get_db()
    if con:
        my_cursor = con.cursor()
        if title and description and time:
            my_cursor.execute(
                "INSERT INTO tasks (title, description, time) VALUES (?, ?, ?)", 
                (title, description, time)
            )
            con.commit()
            con.close()
            return read_root()
        else:
            con.close()
            raise HTTPException(status_code=400, detail="Missing required fields")
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database")

@app.delete("/items/{title}")
def delete_root(title: str):
    con = get_db()
    if con:
        my_cursor = con.cursor()
        if title:
            my_cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
            con.commit()
            con.close()
            return {"message": "Item deleted"}
        else:
            con.close()
            raise HTTPException(status_code=404, detail="Item not found")
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database")

@app.put("/items/{title}")
def update_root(title: str = Path(...), description: str = Form(None), time: str = Form(None)):
    con = get_db()
    if con:
        my_cursor = con.cursor()
        if description or time:
            if description:
                my_cursor.execute("UPDATE tasks SET description = ? WHERE title = ?", (description, title))
            if time:
                my_cursor.execute("UPDATE tasks SET time = ? WHERE title = ?", (time, title))
            
            con.commit()
            
            result = my_cursor.execute("SELECT description, time, status FROM tasks WHERE title = ?", (title,))
            task = result.fetchall()
            con.close()
            return [dict(t) for t in task] 
        else:
            con.close()
            raise HTTPException(status_code=400, detail="No update fields provided")
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database")
