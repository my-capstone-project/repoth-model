# repoth-model

REST API to predict model Repoth

## How to use

Create http request with `POST` https://`<cloudrun>`/predict/.
  
**input** with `form-data`
- key   : file
- value : `<image>`

**output**
```json
{
  "filename": "<image-name>",
  "status"  : "<normal | pothole>",
  "classes" : "[<number-of-predict-result]"
}
```

### Example of output:
```json
{
  "filename": "road_smg.jpg",
  "status"  : "pothole",
  "classes" : "[0.344]"
}
```
