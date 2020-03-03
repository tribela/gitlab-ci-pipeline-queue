gitlab-ci-pipeline-queue
====

This is inspired from https://github.com/flegall/gitlab-ci-pipeline-queue
But this uses APIv4 and python


## How to use

* Create an api access token and provide it as a secret variable named `GITLAB_API_TOKEN`
* Modify your .gitlab-ci.yml to add additional stage and job

    ```
    stages:
    - lock

    lock:
      stage: lock
      image: python:3.7-alpine
      script:
        - pip install gitlab-ci-pipeline-queue
        - env PYTHON_UNBUFFERED=1 gitlab-ci-pipeline-queue
    ```
