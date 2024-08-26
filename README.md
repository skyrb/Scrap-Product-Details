// Have implement the caches and for notification and data storage I could have used config factory pattern to create the concrete object as per need but for I have intitlize manually in code. 

### For Dependency install 
    `pip install -r requirements.txt`


### Command to run code
    `python3 -m uvicorn main:app --reload --port 8081`


### Curl for Scrap Result
        ```  curl --location 'http://127.0.0.1:8001/api/scrape' \
--header 'Authorization: Bearer static_token' \
--header 'Content-Type: application/json' \
--data '{
    "num_pages":5
}' ```