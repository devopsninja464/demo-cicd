pipeline {
  agent any

  parameters {
    string(name: 'PREFIX',     defaultValue: '', description: 'Student prefix e.g. john')
    string(name: 'MYAPP_PORT', defaultValue: '', description: 'App port e.g. 8187')
  }

  stages {
    stage('Checkout') {
      steps {
        sh """
          rm -rf \${WORKSPACE}/app
          git clone https://github.com/devopsninja464/demo-cicd \${WORKSPACE}/app
          ls \${WORKSPACE}/app
        """
      }
    }
    stage('Test') {
      steps {
        sh """
          cd \${WORKSPACE}/app
          grep -q AvantiIQ app.py   && echo PASS: content check OK
          grep -q HTTPServer app.py && echo PASS: server check OK
          grep -q do_GET app.py     && echo PASS: handler check OK
          test ! -f \${WORKSPACE}/BREAK && echo PASS: no break flag || (echo FAIL: BREAK flag found -- fix your code && exit 1)
        """
      }
    }
    stage('Build Docker Image') {
      steps {
        sh """
          cd \${WORKSPACE}/app
          docker build -t ${params.PREFIX}-cicd-img:latest .
          echo Image built: ${params.PREFIX}-cicd-img:latest
        """
      }
    }
    stage('Deploy') {
      steps {
        sh """
          docker stop ${params.PREFIX}-cicd-app 2>/dev/null || true
          docker rm   ${params.PREFIX}-cicd-app 2>/dev/null || true
          docker run -d -p ${params.MYAPP_PORT}:8000 \
            --name ${params.PREFIX}-cicd-app \
            ${params.PREFIX}-cicd-img:latest
          sleep 3
        """
        sh '''
          APP_IP=$(docker inspect $(docker ps -qf name=-cicd-app) \
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
