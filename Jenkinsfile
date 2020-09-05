 pipeline {
        agent any
        stages{
            stage('Upload zip to nexus'){
            steps{
                nexusArtifactUploader artifacts: [
                    [
                        artifactId: 'Capstone-sample',
                        classifier: '',
                        file: 'Blogger/',
                        type: 'zip'
                    ]
                  ],
                  credentialsId: 'nexus_pass',
                  groupId: 'nexus-artifacts',
                  nexusUrl: '10.128.0.10:8081',
                  nexusVersion: 'nexus3',
                  protocol: 'http',
                  repository: 'devops-capstone',
                  version: '1.0.0'
            }
          }
       }
   }