import boto3
import os


def upload_to_s3(s3, local_file, s3_key):
    '''
    upload the file to s3 bucket
    parameters:
        local_file: the absolute path of the file to upload
        s3_key: the relative path of the file within the [local_file] directory
    '''
    bucket_name = "mirrulations-test-bucket" # change the bucket name if needed
    s3.upload_file(local_file, bucket_name, s3_key)


def connect_to_s3(profile):
    '''
    connect to s3
    '''
    session = boto3.Session(profile_name=profile)
    return session.client("s3")


def main():
    '''
    get each file in the data directory and its relative path within the directory
    uses the relative path as the file's s3 key.
    '''
    mb_uploaded = 0 # running total of MB uploaded for logging
    files_uploaded = 0 # running total of files uploaded for logging

    s3 = connect_to_s3("mirrulations_client") # change the profile name if needed

    data_dir = os.path.expanduser("~/data/data") # get the absolute path of the data directory

    for root, dirs, files in os.walk(data_dir):
        for filename in files:
            local_path = os.path.join(root, filename) # get the full absolute path of the file
            s3_path = os.path.relpath(local_path, data_dir) # get the relative path of the file from within the data directory 
            upload_to_s3(s3, local_path, s3_path)
            
            # below is just for logging purposes
            mb_uploaded += os.path.getsize(local_path) / 10**6 # convert bytes to MB
            files_uploaded += 1
            if files_uploaded % 500 == 0:  # log every 500 files
                print(f"{mb_uploaded:.2f} MB uploaded, {files_uploaded} files uploaded, Last S3 Object uploaded : {s3_path}")
               


if __name__ == "__main__":
    main()
