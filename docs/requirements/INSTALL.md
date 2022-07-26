# Installation instructions

## Conda Installation

Install environment with:

```bash
$ : conda env create -f environment.yml
```

## Docker

This section describes how to build and push the docker image for setting up Jupyter Hub in AWS SageMaker.

### Initial Steps aka Setting up AWS the right way

Steps:

1. Install and configure [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html). We recommend installing the version 2. See the [configuration instruction](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to set up the credentials.

2. Add yourself as admin for the account by following [these instructions](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html). If you are not too sure what a is a root account, as an example we will consider the account with email `sih.training@sydney.edu.au` login as the root, and a login account with email `sergio.pintaldi@sydney.edu.au` as the user account. So in the instruction above you need to add a user with email `sergio.pintaldi@sydney.edu.au` as administrator.

3. Continue with the creation of a set of access and secret access keys by following [these info](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds).

4. Use these newly created __access key and secret access key__ in your AWS CLI. If you already have a `default` profile in your AWS CLI, or in general we recommend to add such credential as a profile:

    ```bash
    $ : aws configure --profile usyd_training
    ```
    This will add a new section in your credential file (see detail [description](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)).

    __NOTE__: If your are not sure wich default region to use, remember to pick the region on which the services such as EC2 and SageMaker will run. We choose `us-east-2` as would give a cheaper billing.

### Build and Push the Docker image to AWS

__Note__: `ACCOUNT_ID` is not `AWS_ACCESS_KEY_ID`! The `ACCOUNT_ID` can be obtained by logging in as the root user (e.g. `sih.training@sydney.edu.au`) and selecting _"My Account"_ from the menu in the top right corner with the root user name (e.g. _"SIH Training"_).
    Also make sure the `REGION` is the same of the one saved in the aws profile.

Steps:

1. Build image with:
    ```bash
    $ : REGION=<aws-region>
    $ : ACCOUNT_ID=<account-id>
    $ : IMAGE_NAME=geopy
    $ : cd requirements
    $ : aws --profile usyd_training ecr get-login-password | \
        docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
    $ : docker build . -t ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${IMAGE_NAME}:latest
    ```

2. Create a repository on ECR if not existent (we are using the same name of the image - [detailed instructions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)):
    ```bash
    $ : aws --profile usyd_training ecr create-repository \
        --repository-name ${IMAGE_NAME} \
        --image-scanning-configuration scanOnPush=true \
        --region ${REGION}
    ```

3. Push the docker image to AWS:
    ```bash
    $ : docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${IMAGE_NAME}:latest
    ```

4. Attach the image to SageMaker studio via portal as described [online](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-attach.html?icmpid=docs_sagemaker_console_studio).

### Test image locally to check everything works

```bash
$ : docker run -it --rm -p 127.0.0.1:8888:8888 ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${IMAGE_NAME}:latest jupyter lab --no-browser --ip=0.0.0.0
```
