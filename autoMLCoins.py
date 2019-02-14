
import os
from google.cloud import automl_v1beta1
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"

def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

if __name__ == '__main__':
  file_path = "train810.png"
  project_id = "clcimagedetect-231308"
  model_id = "ICN2235805741960101156"

  with open(file_path, 'rb') as ff:
    content = ff.read()

  print (get_prediction(content, project_id,  model_id))