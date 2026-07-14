import fastapi as FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"text":"Hello!"}


## TODO Upload Videos
## -> sign URL for S3 direct upload
## -> store video metadata in DB
## -> PUT to Queue for procoessing
## -> Thumbnail

## TODO Fetch Videos
## -> homepage
## -> trending - last 7 days
## -> search
## -> infinite scroll


## TODO Task Management - Nureddin @Nooreldien
## TODO Likes API
## TODO Track views counter
## TODO 
