def COLOR_MAP = [
    'SUCCESS': 'good', 
    'FAILURE': 'danger',
]
def getBuildUser() {
    return currentBuild.rawBuild.getCause(Cause.UserIdCause).getUserId()
}
pipeline {
    environment {
        // test variable: 0=success, 1=fail; must be string
        doError = '0'
        BUILD_USER = ''
    }
    agent any 
    stages {
        stage('Test') { 
            steps {
                sh label: '', script: '''cd Blogger
                python3 -m coverage run --source tests,project,config -m  pytest -v
                python3 -m coverage xml -i
                cd ../selenium
                python3 test_login.py'''
            }
        }
        stage('SonarQube analysis and created zip file') {
               environment {
              scannerHome= tool name: 'SonarQube Scanner 3.0.2.768', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
             } 
             steps {
                  withSonarQubeEnv("Scan") {
                   sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=Project -Dsonar.projectName=Blogger${BUILD_NUMBER} -Dsonar.projectVersion=1.0 -Dsonar.sources=Blogger -Dsonar.exclusions=**/*.html,**/*.css,**/*.js -Dsonar.sourceEncoding=UTF-8 -Dsonar.python.coverage.reportPath=Blogger/coverage.xml '''
                  }
  
                 sh label: '', script: ' zip Blogger.zip -r Blogger'
           }
         }
         stage('Jfrog_upload') { 
            steps {
                 sh label: '', script: 'curl -uadmin:admin@123 -T *.zip "http://localhost:8083/artifactory/example-repo-local/Capstone_${BUILD_NUMBER}/"'
            }
        }
         stage('Deploy') { 
            steps {
                ansiblePlaybook installation: 'ansible', playbook: 'docker.yml'
            }
        }
         stage('Error') {
            // when doError is equal to 1, return an error
         when {
                expression { doError == '1' }
         }
         steps {
                echo "Failure :("
                error "Test failed on purpose, doError == str(1)"
            }
        }
        stage('Success') {
            // when doError is equal to 0, just print a simple message
        when {
                expression { doError == '0' }
         }
        steps {
                echo "Success :)"
            }
        }
        
    }   
            // Post-build actions
    post {
         always {
           script {
              BUILD_USER = getBuildUser()
            }
            echo 'I will always say hello in the console.'
            slackSend channel: 'capstone-project',
                color: COLOR_MAP[currentBuild.currentResult], tokenCredentialId: 'slack-key', 
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} by ${BUILD_USER}\n More info at: ${env.BUILD_URL}"
        }
    }
  }
