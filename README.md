copy_to_s3 will copy the entire directory structure from ~/data/data into an S3 bucket called mirrulations-data. 

- In ~/.aws you will need a file called credentials which will contain the following:

	`[<CLIENT_NAME>]`
	
	`aws_access_key_id = <ACCESS_KEY>`
	
	`aws_secret_access_key = <SECRET_ACCESS_KEY>`
	
- Replace all <> with appropriate information. 
