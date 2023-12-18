import dotenv
import uvicorn

if __name__ == '__main__':
    dotenv.load_dotenv('.env')
    uvicorn.run('app:app', reload=True)
