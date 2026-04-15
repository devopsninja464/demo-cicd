pipeline {
  agent any

  parameters {
    string(name: 'PREFIX',     defaultValue: '', description: 'Student prefix')
    string(name: 'MYAPP_PORT', defaultValue: '', description: 'App port')
  }

  environment {
    PREFIX     = "${params.PREFIX}"
    MYAPP_PORT = "${params.MYAPP_PORT}"
    APP_DIR    = "${WORKSPACE}/app"
  }

  stages {
    stage('Checkout') {
      steps {
        sh '''
          rm -rf ${APP_DIR}
          git clone https://github.com/devopsninja464/demo-cicd ${APP_DIR}
          ls ${APP_DIR}
        '''
      }
    }
    stage('Test') {
      steps {
        sh '''
          cd ${APP_DIR}
          grep -q AvantiIQ app.py  && echo PASS: content check OK
          grep -q HTTPServer app.py && echo PASS: server check OK
          grep -q do_GET app.py    && echo PASS: handler check OK
        '''
      }
    }
    stage('Build Docker Image') {
      steps {
        sh '''
          cd ${APP_DIR}
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
            --format '{{.NetworkSettings.Networks.bridge.IPAddress}}')
          echo "Container IP: $APP_IP"
          STATUS=$(curl -o /dev/null -w "%{http_code}" -s http://$APP_IP:8000)
          echo "HTTP Status: $STATUS"
          if [ "$STATUS" = "200" ]; then
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
    success { echo 'PIPELINE GREEN' }
    failure { echo 'PIPELINE RED' }
  }
}
