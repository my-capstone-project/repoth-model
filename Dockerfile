FROM google/cloud-sdk:alpine as bucket
ARG KEY_FILE
ARG GCLOUD_PROJECT_STG
ARG GCLOUD_BUCKET
ARG VERSION
WORKDIR /models

RUN echo ${KEY_FILE} | base64 -d > gcloud.json
RUN gcloud auth activate-service-account --key-file gcloud.json
RUN gcloud config set project ${GCLOUD_PROJECT_STG}
RUN gsutil -m cp -r ${GCLOUD_BUCKET}/${VERSION}/model.h5 /models

FROM tensorflow/tensorflow
RUN pip install Pillow fastapi uvicorn[standard] python-multipart
WORKDIR /app
COPY . ./
COPY --from=bucket /models .
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]