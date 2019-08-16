# Flask API


###############################################
##    30 July 2019 Added by Samanvay   START
###############################################

HOW TO DEPLOY MIRAI ON FRESH INSTANCE

1) Create new instance

2) Go to instance using gcloud command

3) Go to root user's home directory:

    sudo su -
    
    cd /root
    
4) Check Default Python Version (should be 3.x): 

    python3 -V
    
5) Update & upgrade apt: 

    sudo apt update
    
    sudo apt -y upgrade
    
6) Install essential Python packages: 

    sudo apt install -y python3-pip
    
    sudo apt install build-essential libssl-dev libffi-dev python3-dev
    
    sudo apt install -y python3-venv
    
7) Create virtual environment & source it: 

    python3 -m venv env
    
    source env/bin/activate
    
8) Create Mirai directory structure: 

    mkdir mirai
    
    mkdir mirai/live mirai/qa

9) Pull github code in both live and qa directories:
    (only steps for "live" directory are shown here, follow the same steps for "qa")
    
    cd mirai/live
    
    git clone https://github.com/el-fudo/jts-flask-api
    
    cd jts-flask-api
    
    git checkout --track remotes/origin/new_flow
    
    pip freeze > requirements.txt
    
    pip install -r requirements.txt
    
    pip install mysql-connector
    
    pip install requests
    
    pip install bs4
    
10) Configure SSL certificate:

    sudo apt-get install apache2
    
    sudo /etc/init.d/apache2 start
    
    sudo apt-get install certbot
    
    sudo certbot certonly --webroot -w /var/www/html -d mirai.jtsboard.com
    
    cp /etc/letsencrypt/archive/mirai.jtsboard.com/fullchain1.pem .
    
    cp /etc/letsencrypt/archive/mirai.jtsboard.com/privkey1.pem .
    
11) Set up cron:

    cd /root
    
    git clone https://github.com/samanvayzed/crons.git
    
    Add this line to cron file: "* * * * * /root/crons/live_minutely_cron.sh"
    
12) Make changes to main.py:

    cd mirai/live/jts-flask-api
    
    A) Change DB name and password in main.py:
    
        def create_sql_conn():
            mydb = mysql.connector.connect(
                                   host="34.85.64.241",
                                   user="jts",
                                   passwd="Jts45678@?", ***CHANGE THIS***
                                   database="jtsboard_jts", ***CHANGE THIS***
                                   buffered=True
                                   )
            #mycursor = mydb.cursor(buffered=True)
            mycursor = mydb.cursor()
            return mydb,mycursor
      
    B) Change DB name and password in main.py:
        
        if __name__ == '__main__':
            app.run(debug=True)   ***COMMENT THIS***                                                 # For Dev Server  
            #context = ('fullchain1.pem','privkey1.pem')  ***UNCOMMENT THIS***                      # For QA and Live Server
            #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5001)                       # For QA Server 
            #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5000) ***UNCOMMENT THIS***  # For Live Server
            
13) Kill Mirai process (cron will automatically restart it)

    ps -ef | grep live
    
    kill -9 (2 process ids)
    
    Wait for 1 min


HOW TO UPDATE MIRAI ON EXISTING INSTANCE


1) Go to instance using gcloud command

2) Go to root user's home directory: 

    sudo su -
    
    cd /root
    
    
3) Update Code:

    cd mirai/live/jts-flask-api
    
    git reset --hard
    
    git pull

    
4) Make changes to main.py:

    cd mirai/live/jts-flask-api
    
    A) Change DB name and password in main.py:
    
        def create_sql_conn():
            mydb = mysql.connector.connect(
                                   host="34.85.64.241",
                                   user="jts",
                                   passwd="Jts45678@?",  ***CHANGE THIS***
                                   database="jtsboard_jts", *** CHANGE THIS***
                                   buffered=True
                                   )
            #mycursor = mydb.cursor(buffered=True)
            mycursor = mydb.cursor()
            return mydb,mycursor
      
    B) Change DB name and password in main.py:
    
        if __name__ == '__main__':
            app.run(debug=True)   ***COMMENT THIS***                                                # For Dev Server  
            #context = ('fullchain1.pem','privkey1.pem')  ***UNCOMMENT THIS***                      # For QA and Live Server
            #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5001)                       # For QA Server 
            #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5000) ***UNCOMMENT THIS***  # For Live Server
            
5) Kill Mirai process (cron will automatically restart it)

    ps -ef | grep live
    
    kill -9 (2 process ids)
    
    Wait for 1 min

      
    
   
###############################################
##    30 July 2019 Added by Samanvay   END
###############################################
    
    
    
    
    
    
    
    
    
























steps:

step 1:
install git:

sudo apt-get update
sudo apt-get install git

step2:
install pip3:

sudo apt install python3-pip

step3:
crate virtualenv:
pip3 install virtualenv

python3 -m virtualenv env
source env/bin/activate

rm -rf mydir

stes:
clone flask app model from git:
git clone https://github.com/zedmanish/dtsales.git


step4:
pip3 install -r requirements.txt

step5:

if we get permission error:
on deploying:

gcloud auth login

step6:
finally deploy:

gcloud app deploy
