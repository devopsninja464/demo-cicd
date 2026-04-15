pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''
          rm -rf /tmp/${PREFIX}_cicd
          git clone https://github.com/devopsninja464/demo-cicd /tmp/${PREFIX}_cicd
          ls /tmp/${PREFIX}_cicd
        '''
      }
    }
    stage('Test') {
      steps {
        sh '''
          cd /tmp/${PREFIX}_cicd
          python3 -m py_compile app.py && echo PASS: syntax OK
          grep -q AvantiIQ app.py && echo PASS: content check OK
        '''
      }
    }
    stage('Build Docker Image') {
      steps {
        sh '''
          cd /tmp/${PREFIX}_cicd
          docker build -t ${PREFIX}_cicd-img:latest .
          echo Image built: ${PREFIX}_cicd-img:latest
        '''
      }
    }
    stage('Deploy') {
      steps {
        sh '''
          docker stop ${PREFIX}_cicd-app 2>/dev/null || true
          docker rm   ${PREFIX}_cicd-app 2>/dev/null || true
          docker run -d -p ${MYAPP_PORT}:8000 --name ${PREFIX}_cicd-app ${PREFIX}_cicd-img:latest
          sleep 3
          APP_IP=$(docker inspect $(docker ps -qf name=_cicd-app) \
            --format {{.NetworkSettings.Networks.bridge.IPAddress}})
          echo Container IP: $APP_IP
          STATUS=$(curl -o /dev/null -w %{http_code} -s http://$APP_IP:8000)
          echo HTTP Status: $STATUS
          if [ $STATUS = 200 ]; then
            echo DEPLOY OK
          else
            echo DEPLOY FAILED
            exit 1
          fi
        '''
      }
    }
  }
  post {
    success { echo PIPELINE GREEN }
    failure { echo PIPELINE RED }
  }
}
