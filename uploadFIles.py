import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
      

    def upload_file(self, file_from, file_to):

        for root, dirs, file in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
            
            relative_path = os.paath.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.BuJqrIPryYk48vl33Qp2nkZ0z6p2o0jfPGG9SWDoaSaYBqSDdQHQV3AdJSOLhaymRGx_JpZTipQP4bPNDPvv03qvX0-16Xnk5P8ox0wadmtH7NLVH0zLHpLTSSikxR5e2z4r0yywIQRw"
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer :- "))
    file_to = input("Enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("File have been move!")

if __name__ == '__main__':
    main()
