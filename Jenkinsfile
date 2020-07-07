def projectName = 'cicd'
def imageName = 'jenkins-agent-python'
def imageVersion = '1.0.0'

pipeline{
    agent { label 'maven' }

    stages{
        stage('Create BuildConfig') {
            when {
                expression {
                    openshift.withCluster() {
                        openshift.withProject(projectName) {
                            return !openshift.selector("bc", imageName).exists();
                        }
                    }
                }
            }
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject(projectName) {
                            openshift.newBuild("--name=${imageName}", "--strategy=docker","--binary=true", "--to='${imageName}:${imageVersion}'")
                        }
                    }
                }
            }
        }
        stage ('Build Image') {
            steps{
                script {
                    openshift.withCluster() {
                        openshift.withProject(projectName) {
                            def build = openshift.selector("bc", imageName).startBuild("--from-dir=.")
                            build.logs('-f')
                            if (build.object().status.phase == 'Failed'){
                              currentBuild.result = "FAILURE"
                              error('FAILURE')
                            }
                        }
                    }
                }
            }
        }
    }
}
