from fastapi import FastAPI
app=FastAPI(title='fr')

@app.get('/')
def hi():
    return {'msg':'fr'}
