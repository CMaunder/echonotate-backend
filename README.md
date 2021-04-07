# To deploy to production

- push changes via git
- log into server with: ssh -i tabscribe-predict-notes.pem ubuntu@ec2-18-130-228-3.eu-west-2.compute.amazonaws.com
- ensure in root of directory, then git pull
- then: pip install -r requirements.txt
- then: sudo systemctl restart tabscribe-predict-notes
