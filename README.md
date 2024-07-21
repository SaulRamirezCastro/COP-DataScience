## COP-DataScience

A personal demo to show how you can track metadata for files ingest and transform them in Aws.

Project to tack all the metadata files ingested in Aws S3, using Aws lambda function to apply some transformations and put in S3. To track this, we use an Aws lambda function triggered by Aws Sqs and store the information in the Aws Dynamo table.

### Aws Diagram.

![Alt text](diagram/COP-data.drawio.png?raw=true "Aws Diagram.")

### Project Structure
```bash
.
├── README.md
├── convert_etl
│         ├── config.yml
│         ├── convert_file.py
│         ├── lambda_funtion.py
│         └── test
│            └── test_convert.py
├── deploy
├── diagram
│        └── COP-data.drawio.png
└── metadata
    ├── config.yml
    ├── lambda_function.py
    ├── metadata.py
    └── test
        └── test_metadata.py

```

### Technologies

- Aws S3
- Aws Lambda(Python)
- Aws SQS
- Aws Dynamo

### TO DO:
-[X] Create Aws Lambda to Convert csv file
-[X] Create Aws Lambda to write the metadata into Dynamo
-[ ] Add Aws Sqs as Message queue
-[ ] Add Terraform to deploy the project.
 

