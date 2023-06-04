# Repoth model

REST API to predict model Repoth

## Endpoint
http://repoth.my.id:8000

## Predict
- URL
  - `/predict`
- Method
  - `POST`
- Request Body
  - `image` as `file`
- Response

```json
{
    "error": false,
    "message": "Success Predict",
    "result": {
        "filename": "jalan.jpg",
        "pothole": true,
        "url": "https://storage.googleapis.com/potholeimages/jalan.jpg"
    }
}
```
